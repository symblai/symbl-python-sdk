from symbl.Conversations import Conversation
from symbl.AuthenticationToken import get_api_client
from symbl_rest import AsyncApi as async_api_rest
from symbl.jobs_api.Job import Job


class Audio():

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
    def process_file(self, credentials=None, file_path:str = None, content_type:str='', wait:bool=True):
        '''
            audio files to be analyzed
            returns Job object
        '''
        file = open(file_path, 'rb')
        audio_file = file.read()
        response = self.async_api_rest.add_audio(body=audio_file, content_type=content_type)
        print("Job with jobId " + response.job_id + " started!")

        return Conversation(response.conversation_id, response.job_id, wait=wait, credentials=credentials)

    @initialize_api_client
    def process_url(self, credentials=None, url : str = None, wait: bool = False):
        '''
            url of audio file to be analyzed
            returns Job object
        '''
        response = self.async_api_rest.add_audio_url(body={ 'url': url })
        print("Job with jobId " + response.job_id + " started!")

        return Conversation(response.conversation_id, response.job_id, wait=wait, credentials=credentials)
        

    @initialize_api_client
    def append_file(self, credentials=None, file_path:str = None, conversation_id:str = None, content_type:str='', wait:bool=True):
        '''
            audio files to be appended
            returns Job object
        '''
        file = open(file_path, 'rb')
        audio_file = file.read()
        response = self.async_api_rest.append_audio(body=audio_file, content_type=content_type, conversationId= conversation_id)
        print("Job with jobId " + response.job_id + " started!")

        return Conversation(response.conversation_id, response.job_id, wait=wait, credentials=credentials)
  
    @initialize_api_client  
    def append_url(self, credentials=None, url : str = None, conversation_id:str = None, wait: bool = False):
        '''
            url of audio file to be appended
            returns Job object
        '''
        response = self.async_api_rest.append_audio_url(body={ 'url': url }, conversation_id=conversation_id)
        print("Job with jobId " + response.job_id + " started!")

        return Conversation(response.conversation_id, response.job_id, wait=wait, credentials=credentials)
