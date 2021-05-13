from symbl.configs.configs import SYMBL_WEBSOCKET_BASE_PATH, X_API_KEY_HEADER
from symbl.conversations_api.ConversationsApi import ConversationsApi
import json
import threading
import websocket
from symbl.AuthenticationToken import get_api_header

class Connection():

    def __init__(self, conversationId: str, connectionId: str, resultWebSocketUrl: str, eventUrl: str, credentials=None):
        
        self.conversation_id = conversationId
        self.credentials = credentials
        self.connectionId = connectionId
        self.resultWebSocketUrl = resultWebSocketUrl
        self.eventUrl = eventUrl
        access_token = get_api_header(self.credentials).get(X_API_KEY_HEADER)
        self.header = "{}:{}".format(X_API_KEY_HEADER, access_token)
        self.connection = websocket.WebSocket()

    def async_subscribe(self, eventCallbacks: dict):
        print("Eshtablishing connection")
        # print("Connecting to " + str( SYMBL_WEBSOCKET_BASE_PATH + self.connectionId) + " with api header ", self.header)
        # print("Eshtablishing connection", self.connection)
        self.connection.connect(url=SYMBL_WEBSOCKET_BASE_PATH + self.connectionId, header=[self.header])
        print("Connection Eshtablished", self.connection)
        while True:
            try:
                data = self.connection.recv()
                print(data)
                if data != None and type(data) == str:  
                    json_data = json.loads(data)
                    if 'type' in json_data and json_data['type'] in eventCallbacks:
                        eventCallbacks[json_data['type']](data) 
            except Exception as error:
                print(error)
                break

    def subscribe(self, eventCallbacks: dict):
        thread = threading.Thread(target=self.async_subscribe, args=(eventCallbacks,))
        thread.start()


    def async_stop(self):
        while self.connection != None:
            self.connection.connect(url=SYMBL_WEBSOCKET_BASE_PATH + self.connectionId, header=[self.header])
            self.connection.send(payload={
                'type': 'stop_request'
            })

    def stop(self):
        thread = threading.Thread(target=self.async_stop, args=())
        thread.start()