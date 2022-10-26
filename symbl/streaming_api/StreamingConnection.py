from symbl.Conversations import Conversation
from symbl.utils.Logger import Log
from symbl.utils.Decorators import wrap_keyboard_interrupt
from symbl.utils.Threads import Thread
from time import sleep
import json
import websocket
from pyogg import OpusBufferedEncoder

class StreamingConnection():

    def __init__(self, url: str, connectionId: str, start_request: dict):
        self.conversation = Conversation(None)
        self.connectionId = connectionId
        self.url = url
        self.event_callbacks = {}
        self.start_request = start_request
        self.connection = None
        self.__connect()
        self.opus_encoder = OpusBufferedEncoder()
        self.opus_encoder.set_application("voip")
        self.opus_encoder.set_sampling_frequency(48000)
        self.opus_encoder.set_channels(1)
        self.opus_encoder.set_frame_size(20)


    def __connect(self):
        if self.connection == None:

            self.connection = websocket.WebSocketApp(url=self.url, on_message=lambda this, data: self.__listen_to_events(data), on_error=lambda this, error: Log.getInstance().error(error))

            Thread.getInstance().start_on_thread(target=self.connection.run_forever)
            conn_timeout = 5
            while not self.connection.sock.connected and conn_timeout:
                sleep(1)
                conn_timeout -= 1

            self.connection.send(json.dumps(self.start_request))
    
    def __set_conversation(self, conversationId: str):
        self.conversation = Conversation(conversationId)

    def __listen_to_events(self, data):
        try:
            decoded_data = data if type(data) == str else data.decode('utf-8')
            json_data = json.loads(decoded_data)
            if 'type' in json_data and json_data['type'] == 'message' and 'type' in json_data['message'] and json_data['message']['type'] == "conversation_created":
                self.__set_conversation(str(json_data['message']['data']['conversationId']))
                Log.getInstance().info("Conversation id is {}".format(str(json_data['message']['data']['conversationId'])))
            elif 'type' in json_data and json_data['type'] == 'message' and 'type' in json_data['message'] and json_data['message']['type'] == "started_listening":
                Log.getInstance().info("Started Listening...")
            elif 'type' in json_data and json_data['type'] in self.event_callbacks:
                self.event_callbacks[json_data['type']](json_data) 
        except Exception as error:
            Log.getInstance().error(error)
            
    def subscribe(self, event_callbacks: dict):
        self.event_callbacks = event_callbacks
        
    def stop(self):
        if self.connection != None:
            stop_payload = {'type': 'stop_request'}
            self.connection.send(str(stop_payload))
    
    @wrap_keyboard_interrupt
    def send_audio(self, data):
        if self.connection != None:

            if self.start_request['config']['speechRecognition']['encoding'] == 'OPUS':

                self.opus_encoder.buffered_encode(
                    memoryview(bytearray(data)),
                    callback=lambda encoded_packet, *args: self.connection.send(
                        encoded_packet.tobytes(),
                        opcode=websocket.ABNF.OPCODE_BINARY))

            elif self.start_request['config']['speechRecognition']['encoding'] == 'LINEAR16':

                self.connection.send(data, opcode=websocket.ABNF.OPCODE_BINARY)


    @wrap_keyboard_interrupt
    def send_audio_from_mic(self, device=None):
        import sounddevice as sd
        samplerate = self.start_request['config']['speechRecognition']['sampleRateHertz']
        with sd.InputStream(blocksize=4096, samplerate=samplerate, channels=1, callback= lambda indata, *args: self.send_audio(indata.copy().tobytes()), dtype='int16', device=device):
            while True:
                pass