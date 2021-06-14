from symbl import StreamingConnection
from symbl.configs.configs import SYMBL_STREAMING_API_FORMAT
from symbl.AuthenticationToken import get_access_token
import websocket
import base64
import random
import string

class StreamingApi():
    def __init__(self):
        '''
            It will initialize the ConversationsApi class
        '''
        pass


    def start_connection(self, credentials=None, speaker=None, insight_types=None, config={}):
        randomId = bytes(''.join(random.choices(string.ascii_uppercase +string.digits, k=12)), 'utf-8')
        id = base64.b64encode(randomId).decode("utf-8")
        url = SYMBL_STREAMING_API_FORMAT.format(id, get_access_token(credentials=credentials))
        
        if type(config) != dict:
            raise TypeError("config should be of type dict")
        
        config_object = {
            "confidenceThreshold": 0.5,
            "languageCode": 'en-US',
            "speechRecognition": {
                "encoding": 'LINEAR16',
                "sampleRateHertz": 44100,
            }
        }

        for key in config.keys():
            config_object[key] = config[key]

        start_request = {
            "type": "start_request",
            "insightTypes": [] if insight_types == None else [] if type(insight_types) != list else insight_types,
            "speaker": speaker,
            "config": config_object
        }
    
        return StreamingConnection(url= url, connectionId=id, start_request=start_request)

    def stop_listening(self, url: str):
        connection = websocket.WebSocketApp(url=url)
        stop_payload = {'type': 'stop_request'}
        connection.send(str(stop_payload))