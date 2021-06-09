from symbl.Conversations import Conversation
from symbl.utils.Logger import Log
from symbl.utils.Decorators import wrap_keyboard_interrupt
from symbl.utils.Threads import Thread
from time import sleep
import json
import websocket

class StreamingConnection():

    def __init__(self, url: str, connectionId: str, start_request: dict):
        self.conversation = Conversation(None)
        self.connectionId = connectionId
        self.url = url
        self.event_callbacks = {}
        self.start_request = start_request
        self.connection = None
        self.__connect()


    def __connect(self):
        if self.connection == None:

            self.connection = websocket.WebSocketApp(url=self.url, on_message=lambda this, data: self.__listen_to_events(data), on_error=lambda error: Log.getInstance().error(error))

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
            if 'type' in json_data and json_data['type'] == 'message' and 'data' in json_data['message'] and 'conversationId' in json_data['message']['data']:
                self.__set_conversation(str(json_data['message']['data']['conversationId']))
                Log.getInstance().info("Conversation id is {}".format(str(json_data['message']['data']['conversationId'])))
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
            self.connection.send(data, opcode=websocket.ABNF.OPCODE_BINARY)

    @wrap_keyboard_interrupt
    def send_audio_from_mic(self, device=None):
        import sounddevice as sd
        with sd.InputStream(blocksize=4096, samplerate=44100, channels=1, callback= lambda indata, *args: self.send_audio(indata.copy().tobytes()), dtype='int16', device=device):
            while True:
                pass