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

    def initialize_api_client(self, function):
        def wrapper(*args, **kw):
            credentials = None
            
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
        

    def startEndpoint(self, endpoint, credentials=None, actions={}, data={}):
        def inner(function):
            @self.initialize_api_client
            def wrapper(*args, **kwrags):
                body = dict()
                body = {
                    "operation": "start", 
                    "endpoint": endpoint, 
                    "actions": actions,
                    "data": data
                }
                try:
                    return function(self.validateAndConnectToEndpoint(body), *args, **kwrags)
                except Exception as e:
                    return function(e)
            return wrapper()
        return inner

    def stopEndpoint(self, body):
        def inner(function):
            @self.initialize_api_client
            def wrapper(*args, **kwrags):
                body["operation"] = "stop"

                if body == None:
                    raise ValueError('endpoint configuration is required.')

                if body["connectionId"] == None:
                    raise ValueError('ConnectionId is invalid, Please enter a valid connectionId to stop')

                try:
                    return function(self.telephony_api_rest.connect_to_endpoint(body), *args, **kwrags)
                except Exception as e:
                    return function(e)
            return wrapper()
        return inner
