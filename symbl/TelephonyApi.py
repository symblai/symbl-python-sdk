from symbl.TelephonyValidators import validateActions, validateEndpoint
from symbl_rest import ConnectionToEndpointApi as telephony_api_rest
from symbl.AuthenticationToken import get_api_client

class TelephonyApi():
    def __init__(self, api_client=None):
        '''
            It will initialize the Telephony class
        '''
        
        self.api_client = api_client
        self.telephony_api_rest = telephony_api_rest(api_client)

    def initialize_api_client(function):
        def wrapper(*args, **kw):
            credentials = None
            self = args[0]
            
            if 'credentials' in kw:
                credentials = kw['credentials']

            api_client = get_api_client(credentials)
            self.api_client = api_client
            self.async_api_rest = telephony_api_rest(api_client)

            function(*args, **kw)
        
        return wrapper

    def validateAndConnectToEndpoint(self, body):
        if body == None:
            raise ValueError('endpoint configuration is required.')

        if "endpoint" not in body :
            raise ValueError('Please enter the endpoint you want to connect.')

        validateEndpoint(body["endpoint"])
        
        validateActions(body["actions"])

        return self.telephony_api_rest.connect_to_endpoint(body)
        
    @initialize_api_client
    def startEndpoint(self, endpoint, credentials=None, actions={}, data={}):
        body = dict()
        body = {
            "operation": "start", 
            "endpoint": endpoint, 
            "actions": actions,
            "data": data
        }

        return self.validateAndConnectToEndpoint(body)

    @initialize_api_client
    def stopEndpoint(self, body):
        body["operation"] = "stop"

        if body == None:
            raise ValueError('endpoint configuration is required.')

        if body["connectionId"] == None:
            raise ValueError('ConnectionId is invalid, Please enter a valid connectionId to stop')

        return self.telephony_api_rest.connect_to_endpoint(body)
