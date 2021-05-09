from symbl import StreamingConnection
from symbl.configs.configs import SYMBL_STREAMING_API_FORMAT
import websocket
import base64
import random
import string
import json
from symbl.AuthenticationToken import get_access_token


class StreamingApi():
    def __init__(self):
        '''
            It will initialize the ConversationsApi class
        '''
        self.connection = websocket.WebSocket(enable_multithread=True)


    def start_listening(self, credentials=None, speaker=None, insight_types=None):
        randomId = bytes(''.join(random.choices(string.ascii_uppercase +string.digits, k=12)), 'utf-8')
        id = base64.b64encode(randomId).decode("utf-8") 
        self.connection.connect(url=SYMBL_STREAMING_API_FORMAT.format(id, get_access_token(credentials=credentials)))
        print("Connected to websocket with id", SYMBL_STREAMING_API_FORMAT.format(id, get_access_token(credentials=credentials)))
        start_request = {
            "type": "start_request",
            "insightTypes": [] if insight_types == None else [] if type(insight_types) != list else insight_types,
            "speaker": speaker,
             "config": {
                "confidenceThreshold": 0.5,
                "languageCode": 'en-US',
                "speechRecognition": {
                    "encoding": 'LINEAR16',
                    "sampleRateHertz": 44100,
                }
            },
        }
        
        self.connection.send(json.dumps(start_request))
        data = ""
        conversationId = None

        while conversationId == None:
            resp_opcode, data = self.connection.recv_data()
            print("Response opcode: " + str(resp_opcode))

            stringData = data.decode('utf-8')
            json_data = json.loads(stringData)
            if 'type' in json_data and json_data['type'] == 'message' and 'data' in json_data['message']:
                conversationId = str(json_data['message']['data']['conversationId'])
                print("Conversation id is ", str(json_data['message']['data']['conversationId']))

        return StreamingConnection(webSocket=self.connection, credentials=credentials, conversationId=conversationId, connectionId=id)
    