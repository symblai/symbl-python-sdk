from symbl.Connection import Connection
from symbl.telephony_api.TelephonyValidators import validateActions, validateEndpoint
from symbl_rest import ConnectionToEndpointApi as telephony_api_rest
from symbl.AuthenticationToken import get_api_client


def initialize_api_client(function):
    def wrapper(*args, **kw):
        credentials = None
        self = args[0]
        
        if 'credentials' in kw:
            credentials = kw['credentials']

        api_client = get_api_client(credentials)
        self.api_client = api_client
        self.async_api_rest = telephony_api_rest(api_client)

        return function(*args, **kw)
    
    return wrapper
class TelephonyApi():
    def __init__(self, api_client=None):
        '''
            It will initialize the Telephony class
        '''
        
        self.api_client = api_client
        self.telephony_api_rest = telephony_api_rest(api_client)

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
    def start_pstn(self, phoneNumber, dtmf=None, credentials=None, actions={}, data={}):
        body = dict()
        body = {
            "operation": "start", 
            "endpoint": {
                "type": "pstn",
                "phoneNumber": phoneNumber,
                "dtmf": dtmf
            }, 
            "actions": actions,
            "data": data,
            "pushSpeakerEvents": True
        }

        return self.validateAndConnectToEndpoint(body, credentials)

    @initialize_api_client
    def start_sip(self, uri, audioConfig={}, credentials=None, actions={}, data={}):
        body = dict()
        body = {
            "operation": "start", 
            "endpoint": {
                "type": "sip",
                "uri": uri,
                "audioConfig": audioConfig
            }, 
            "actions": actions,
            "data": data,
            "pushSpeakerEvents": True
        }

        return self.validateAndConnectToEndpoint(body)

    @initialize_api_client
    def stop(self, connectionId):
        body = dict()
        body["operation"] = "stop"
        body["connectionId"] = connectionId


        if connectionId == None:
            raise ValueError('ConnectionId is invalid, Please enter a valid connectionId to stop')

        return self.telephony_api_rest.connect_to_endpoint(body)
