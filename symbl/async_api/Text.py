from symbl.Conversations import Conversation
from symbl.AuthenticationToken import get_api_client
from symbl_rest import AsyncApi as async_api_rest

def initialize_api_client(function):
    def wrapper(*args, **kw):
        credentials = None
        self = args[0]
        
        if 'credentials' in kw:
            credentials = kw['credentials']

        api_client = get_api_client(credentials)
        self.__async_api_rest = async_api_rest(api_client)

        return function(*args, **kw)
    
    return wrapper

def correct_boolean_values(dictionary: dict):
    for key in dictionary:
        if dictionary[key] == True:
            dictionary[key] = "true"
        elif dictionary[key] == False:
            dictionary[key] = "false"
    return dictionary
    
class Text():

    def __init__(self, api_client=None):
        '''
            It will initialize the Analysis class
            with the object of Initialize Class
        '''
        self.__async_api_rest = async_api_rest(api_client)

    @initialize_api_client
    def process(self, payload : dict, credentials=None, wait: bool = True, parameters={}):
        '''
            Text payload to be analyzed
            returns Conversation object
        '''
        
        if payload == None:
            raise ValueError("Please enter a valid payload.")

        response = self.__async_api_rest.add_text(body=payload, **correct_boolean_values(parameters))
        print("Job with jobId {} for conversationId {} started".format(response.job_id, response.conversation_id))

        return Conversation(response.conversation_id, response.job_id, wait=wait, credentials=credentials)

    @initialize_api_client
    def append(self, payload:dict, conversation_id:str, credentials=None, wait: bool = True, parameters={}):
        '''
            Text payload to be appended
            returns Conversation object
        '''
        if payload == None:
            raise ValueError("Text Payload can not be None")

        if conversation_id == None or len(conversation_id) == 0:
            raise ValueError("Please enter a valid conversationId")

        response = self.__async_api_rest.append_text(conversation_id, body=payload, **correct_boolean_values(parameters))
        print("Job with jobId {} for conversationId {} started".format(response.job_id, response.conversation_id))

        return Conversation(response.conversation_id, response.job_id, wait=wait, credentials=credentials)