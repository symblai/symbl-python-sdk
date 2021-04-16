from symbl.TelephonyValidators import validateActions, validateEndpoint
from symbl_rest import ConnectionToEndpointApi as telephony_api_rest

class TelephonyApi():
    def __init__(self, api_client=None):
        '''
            It will initialize the ConversationsApi class
        '''

        if api_client is None:
            raise ValueError('Please initialize sdk with correct app_id and app_secret.')
        
        self.api_client = api_client
        self.telephony_api_rest = telephony_api_rest(api_client)

    def validateAndConnectToEndpoint(self, body):

        if body == None:
            raise ValueError('endpoint configuration is required.')

        if "endpoint" not in body :
            raise ValueError('Please enter the endpoint you want to connect.')

        validateEndpoint(body["endpoint"])
        
        if "actions" not in body:
            raise ValueError('Please enter the endpoint you want to connect.')
        
        validateActions(body["actions"])

        return self.telephony_api_rest.connect_to_endpoint(body)
    
    def startEndpoint(self, body):
        body["operation"] = "start"

        return self.validateAndConnectToEndpoint(body)

    def stopEndpoint(self, body):
        body["operation"] = "stop"

        if body == None:
            raise ValueError('endpoint configuration is required.')

        if body["connectionId"] == None:
            raise ValueError('ConnectionId is invalid, Please enter a valid connectionId to stop')

        return self.telephony_api_rest.connect_to_endpoint(body)
