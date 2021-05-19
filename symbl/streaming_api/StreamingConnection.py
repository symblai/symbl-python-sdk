from symbl.configs.configs import X_API_KEY_HEADER
import json
import threading
import websocket
import json
from time import sleep

class StreamingConnection():

    def __init__(self, url: str, connectionId: str, start_request: dict):
        
        self.connectionId = connectionId
        self.url = url
        self.event_callbacks = {}
        self.start_request = start_request

        self.connect()


    def connect(self):
        self.connection = websocket.WebSocketApp(url=self.url, on_message=lambda this, data: self.__listen_to_events(data), on_data=lambda this, data: self.__listen_to_events(data), on_error=lambda error: print(error))

        websocket_thread = threading.Thread(target=self.connection.run_forever)
        # websocket_thread.daemon = True
        websocket_thread.start()

        conn_timeout = 5
        while not self.connection.sock.connected and conn_timeout:
            sleep(1)
            conn_timeout -= 1

        self.connection.send(json.dumps(self.start_request))
    
    def set_conversation_id(self, conversationId: str):
        self.conversationId = conversationId

    def __listen_to_events(self, data):
        try:
            decoded_data = data if type(data) == str else data.decode('utf-8')
            json_data = json.loads(decoded_data)
            if 'type' in json_data and json_data['type'] in self.event_callbacks:
                self.event_callbacks[json_data['type']](data) 
            elif 'type' in json_data and json_data['type'] == 'message' and 'data' in json_data['message']:
                self.set_conversation_id(str(json_data['message']['data']['conversationId']))
                print("Conversation id is ", str(json_data['message']['data']['conversationId']))
        except Exception as error:
            print(error)
            
    def subscribe(self, event_callbacks: dict):
        self.event_callbacks = event_callbacks
        
    def stop(self):
        if self.connection != None:
            stop_payload = {'type': 'stop_request'}
            self.connection.send(str(stop_payload))

    def async_send(self, data):
        if self.connection != None:
            self.connection.send(data, opcode=websocket.ABNF.OPCODE_BINARY)

    def send_data(self, data):
        if self.connection != None:
            print('Sending data')
            self.connection.send(data)
    
    def send_audio(self, data):
        thread = threading.Thread(target=self.async_send, args=(data,))
        thread.start()