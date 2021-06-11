from symbl.Connection import Connection
from symbl.telephony_api.TelephonyValidators import validateActions, validateEndpoint
from symbl_rest import ConnectionToEndpointApi as telephony_api_rest
from symbl.utils.Helper import initialize_api_client
class TelephonyApi():
    def __init__(self):
        '''
            It will initialize the Telephony class
        '''

        self.telephony_api_rest = telephony_api_rest()

    def validateAndConnectToEndpoint(self, body, credentials=None):
        if body == None:
            raise ValueError('endpoint configuration is required.')

        if "endpoint" not in body :
            raise ValueError('Please enter the endpoint you want to connect.')

        validateEndpoint(body["endpoint"])
        
        validateActions(body["actions"])

        data = self.telephony_api_rest.connect_to_endpoint(body)
        connectionObject = Connection(connectionId=data.connection_id, conversationId=data.conversation_id, resultWebSocketUrl=data.result_web_socket_url, eventUrl=data.event_url, credentials=credentials)
        
        return connectionObject

    @initialize_api_client
    def start_pstn(self, phone_number, dtmf=None, credentials=None, actions={}, data={}, languages:list=[], timezone:str=None):
        body = dict()
        body = {
            "operation": "start", 
            "endpoint": {
                "type": "pstn",
                "phoneNumber": phone_number,
                "dtmf": dtmf
            }, 
            "actions": actions,
            "data": data,
            "pushSpeakerEvents": True
        }

        if type(languages) == list and len(languages) > 0:
            body['languages'] = languages
        elif type(languages) != list:
            raise TypeError("languages should be a list of string")
        
        if timezone != None:
            if type(timezone) == str:
                body["timezone"] = timezone
            elif type(timezone) != str:
                raise TypeError('timezone should be of type string')

        return self.validateAndConnectToEndpoint(body, credentials)

    @initialize_api_client
    def start_sip(self, uri, audio_config={}, credentials=None, actions={}, data={}, languages:list=[], timezone:str=None):
        body = dict()

        if audio_config == {}:

            audio_config = { 
                "sampleRate": 16000,
                "sampleSize": "16"
            }

        body = {
            "operation": "start", 
            "endpoint": {
                "type": "sip",
                "uri": uri,
                "audioConfig": audio_config
            }, 
            "actions": actions,
            "data": data,
            # "pushSpeakerEvents": True
        }

        if type(languages) == list and len(languages) > 0:
            body['languages'] = languages
        elif type(languages) != list:
            raise TypeError("languages should be a list of string")
        
        if timezone != None:
            if type(timezone) == str:
                body["timezone"] = timezone
            elif type(timezone) != str:
                raise TypeError('timezone should be of type string')

        return self.validateAndConnectToEndpoint(body)

    @initialize_api_client
    def stop(self, connection_id):
        body = dict()
        body["operation"] = "stop"
        body["connectionId"] = connection_id


        if connection_id == None:
            raise ValueError('ConnectionId is invalid, Please enter a valid connectionId to stop')

        return self.telephony_api_rest.connect_to_endpoint(body)
