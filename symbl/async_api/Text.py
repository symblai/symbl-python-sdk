from symbl.Conversations import Conversation
from symbl.AuthenticationToken import get_api_client
from symbl_rest import AsyncApi as async_api_rest
from symbl.jobs_api.Job import Job


class Text():

    def __init__(self, api_client=None):
        '''
            It will initialize the Analysis class
            with the object of Initialize Class
        '''
        self.api_client = api_client
        self.async_api_rest = async_api_rest(api_client)

    def initialize_api_client(function):
        def wrapper(*args, **kw):
            credentials = None
            self = args[0]
            
            if 'credentials' in kw:
                credentials = kw['credentials']

            api_client = get_api_client(credentials)
            self.api_client = api_client
            self.async_api_rest = async_api_rest(api_client)

            return function(*args, **kw)
        
        return wrapper

    @initialize_api_client
    def process(self, credentials=None, text_payload : dict = None, wait: bool = False):
        '''
            Text payload to be analyzed
            returns Job object
        '''

        response = self.async_api_rest.add_text(body=text_payload)
        print("Job with jobId " + response.job_id + " started!")

        return Conversation(response.conversation_id, response.job_id, wait=wait, credentials=credentials)

    @initialize_api_client
    def append(self, credentials=None, text_payload : dict = None, conversation_id:str = None, wait: bool = False):
        '''
            Text payload to be appended
            returns Job object
        '''
        if text_payload == None:
            raise ValueError("Text Payload can not be None")

        if conversation_id == None or len(conversation_id) == 0:
            raise ValueError("Please enter a valid conversationId")

        response = self.async_api_rest.append_text(text_payload, conversation_id)
        print("Job with jobId " + response.job_id + " started!")

        return Conversation(response.conversation_id, response.job_id, wait=wait, credentials=credentials)