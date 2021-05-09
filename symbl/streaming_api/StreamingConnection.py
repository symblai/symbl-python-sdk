from symbl.configs.configs import X_API_KEY_HEADER
import json
import threading
import websocket
from symbl.AuthenticationToken import get_api_header

class StreamingConnection():

    def __init__(self, connectionId: str, webSocket: websocket.WebSocket, conversationId: str,  credentials=None):
        
        self.credentials = credentials
        self.connectionId = connectionId
        self.conversationId = conversationId
        access_token = get_api_header(self.credentials).get(X_API_KEY_HEADER)
        self.header = "{}:{}".format(X_API_KEY_HEADER, access_token)
        self.connection = webSocket


    def set_conversation_id(self, conversationId: str):
        self.conversationId = conversationId

    def async_subscribe(self, eventCallbacks: dict):
        while True:
            opcode = None
            data = None
            try:
                opcode, data = self.connection.recv_data()
            except Exception as error:
                print(error)
                break
            print("data received is ", data, opcode)
            if data != None:
                stringData = data.decode('utf-8')
                try:
                    json_data = json.loads(stringData)
                    if 'type' in json_data and json_data['type'] in eventCallbacks:
                        eventCallbacks[json_data['type']](data) 
                    elif 'type' in json_data and json_data['type'] == 'message' and 'data' in json_data['message']:
                        self.set_conversation_id(str(json_data['message']['data']['conversationId']))
                        print("Conversation id is ", str(json_data['message']['data']['conversationId']))
                except Exception as error:
                    print(error)


    def subscribe(self, eventCallbacks: dict):
        thread = threading.Thread(target=self.async_subscribe, args=(eventCallbacks,))
        thread.start()

    def async_stop(self):
        if self.connection != None:
            stop_payload = {
                'type': 'stop_request'
            }
            self.connection.send(str(stop_payload))

    def stop(self):
        thread = threading.Thread(target=self.async_stop, args=())
        thread.start()

    def async_send(self, data):
        if self.connection != None:
            self.connection.send(data)

    def sendAudio(self, data):
        thread = threading.Thread(target=self.async_send, args=(data,))
        thread.start()