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

    def on_error(self, data):
        print(data)

    def start_listening(self, credentials=None, speaker=None, insight_types=None):
        randomId = bytes(''.join(random.choices(string.ascii_uppercase +string.digits, k=12)), 'utf-8')
        id = base64.b64encode(randomId).decode("utf-8")
        url = SYMBL_STREAMING_API_FORMAT.format(id, get_access_token(credentials=credentials))
        # self.connection = websocket.WebSocketApp(url=SYMBL_STREAMING_API_FORMAT.format(id, get_access_token(credentials=credentials)), on_error=self.on_error)

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

        # websocket_thread = threading.Thread(target=self.connection.run_forever)
        # websocket_thread.daemon = True
        # websocket_thread.start()

        # conn_timeout = 5
        # self.connection.on_message = lambda this, data: print('printing in StreamingApi class', data)

        # while not self.connection.sock.connected and conn_timeout:
        #     print("Is it connected?", conn_timeout)
        #     sleep(1)
        #     conn_timeout -= 1
        
        # print("Is it connected?")

        # self.connection.send(json.dumps(start_request))
    
        return StreamingConnection(url= url, connectionId=id, start_request=start_request)

    def stop_listening(self, url: str):
        connection = websocket.WebSocketApp(url=url)
        stop_payload = {'type': 'stop_request'}
        connection.send(str(stop_payload))