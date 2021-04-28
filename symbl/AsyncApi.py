from symbl.AuthenticationToken import get_api_client
from symbl_rest import AsyncApi as async_api_rest
from functools import wraps
from symbl.Job import Job


class AsyncApi():

    def __init__(self, api_client=None):
        '''
            It will initialize the Analysis class
            with the object of Initialize Class
        '''
        self.api_client = api_client
        self.async_api_rest = async_api_rest(api_client)

    def initialize_api_client(self, function=None):
        def wrapper(*args, **kw):
            credentials = None
            
            if 'credentials' in kw:
                credentials = kw['credentials']
            api_client = get_api_client(credentials)
            self.api_client = api_client
            self.async_api_rest = async_api_rest(api_client)

            function(*args, **kw)
        
        return wrapper

    def submit_text(self, function, credentials=None, text_payload : dict = None, wait: bool = False):

        def inner(function):
            @self.initialize_api_client
            def wrapper(*args, **kw):
                '''
                    Text payload to be analyzed
                    returns Job object
                '''

                response = self.async_api_rest.add_text(body=text_payload)
                print("Job with jobId " + response.job_id + " started!")

                if not wait:
                    job = Job(self.api_client, jobId=response.job_id, conversationId=response.conversation_id, wait=wait)
                    return function(job)

                job = Job(self.api_client, jobId=response.job_id, conversationId=response.conversation_id, wait=wait)
                return function(job.getConversationId())
            return wrapper()
        return inner

    def submit_audio(self, credentials=None, file_path:str = None, content_type:str='', wait:bool=True):
        
        def inner(function):
            @self.initialize_api_client
            def wrapper(*args, **kw):
                '''
                    audio files to be analyzed
                    returns Job object
                '''
                file = open(file_path, 'rb')
                audio_file = file.read()
                response = self.async_api_rest.add_audio(body=audio_file, content_type=content_type)
                print("Job with jobId " + response.job_id + " started!")

                if not wait:
                    job = Job(self.api_client, jobId=response.job_id, conversationId=response.conversation_id, wait=wait)
                    return function(job)

                job = Job(self.api_client, jobId=response.job_id, conversationId=response.conversation_id, wait=wait)
                return function(job.getConversationId())
            return wrapper()
        return inner

    def submit_video(self, credentials=None, file_path:str = None, content_type:str='', wait:bool=True):
        def inner(function):
            @self.initialize_api_client
            def wrapper(*args, **kw):
                '''
                    video files to be analyzed
                    returns Job object
                '''
                file = open(file_path, 'rb')
                audio_file = file.read()
                response = self.async_api_rest.add_audio(body=audio_file, content_type=content_type)
                print("Job with jobId " + response.job_id + " started!")

                if not wait:
                    return function(Job(self.api_client, jobId=response.job_id, 
                    conversationId=response.conversation_id, wait=wait))

                job = Job(self.api_client, jobId=response.job_id, conversationId=response.conversation_id, wait=wait)
                return function(job.getConversationId())
            return wrapper()
        return inner

    def submit_audio_url(self, url : str=None, credentials=None, wait: bool = False):
        def inner(function):
            @self.initialize_api_client
            def wrapper(*args, **kw):
                
                '''
                    url of audio file to be analyzed
                    returns Job object
                '''
                response = self.async_api_rest.add_audio_url(body={ 'url': url })
                print("Job with jobId " + response.job_id + " started!")


                if not wait:
                    job = Job(self.api_client, jobId=response.job_id, conversationId=response.conversation_id, wait=wait)
                    return function(job)

                job = Job(self.api_client, jobId=response.job_id, conversationId=response.conversation_id, wait=wait)
                return function(job.getConversationId())
            return wrapper()
        return inner
        

    def submit_video_url(self, credentials=None, url : str = None, wait: bool = False):
        def inner(function):
            @self.initialize_api_client
            def wrapper(*args, **kw):
                '''
                    url of audio file to be analyzed
                    returns Job object
                '''

                response = self.async_api_rest.add_video_url(body={ 'url': url })
                print("Job with jobId " + response.job_id + " started!")

                if not wait:
                    job = Job(self.api_client, jobId=response.job_id, conversationId=response.conversation_id, wait=wait)
                    return function(job)

                job = Job(self.api_client, jobId=response.job_id, conversationId=response.conversation_id, wait=wait)
                return function(job.getConversationId())
            return wrapper()
        return inner

    def append_text(self, credentials=None, text_payload : dict = None, conversation_id:str = None, wait: bool = False):
        def inner(function):
            @self.initialize_api_client
            def wrapper(*args, **kw):
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

                if not wait:
                    job = Job(self.api_client, jobId=response.job_id, conversationId=response.conversation_id, wait=wait)
                    return function(job)

                job = Job(self.api_client, jobId=response.job_id, conversationId=response.conversation_id, wait=wait)
                return function(job.getConversationId())
            return wrapper()
        return inner

    def append_audio(self, credentials=None, file_path:str = None, conversation_id:str = None, content_type:str='', wait:bool=True):
        def inner(function):
            @self.initialize_api_client
            def wrapper(*args, **kw):
                '''
                    audio files to be appended
                    returns Job object
                '''
                file = open(file_path, 'rb')
                audio_file = file.read()
                response = self.async_api_rest.append_audio(body=audio_file, content_type=content_type, conversationId= conversation_id)
                print("Job with jobId " + response.job_id + " started!")

                if not wait:
                    job = Job(self.api_client, jobId=response.job_id, conversationId=response.conversation_id, wait=wait)
                    return function(job)

                job = Job(self.api_client, jobId=response.job_id, conversationId=response.conversation_id, wait=wait)
                return function(job.getConversationId())
            return wrapper()
        return inner

    def append_video(self, credentials=None, file_path:str = None, conversation_id:str = None, content_type:str='', wait:bool=True):
        def inner(function):
            @self.initialize_api_client
            def wrapper(*args, **kw):
                '''
                    video files to be appended
                    returns Job object
                '''
                if conversation_id == None or len(conversation_id) == 0:
                    raise ValueError("Please enter a valid conversationId")

                file = open(file_path, 'rb')
                video_file = file.read()
                response = self.async_api_rest.appendVideo(body=video_file, content_type=content_type, conversationId=conversation_id)
                print("Job with jobId " + response.job_id + " started!")

                if not wait:
                    job = Job(self.api_client, jobId=response.job_id, conversationId=response.conversation_id, wait=wait)
                    return function(job)

                job = Job(self.api_client, jobId=response.job_id, conversationId=response.conversation_id, wait=wait)
                return function(job.getConversationId())
            return wrapper()
        return inner
  
    def append_audio_url(self, credentials=None, url : str = None, conversation_id:str = None, wait: bool = False):
        def inner(function):
            @self.initialize_api_client
            def wrapper(*args, **kw):
                '''
                    url of audio file to be appended
                    returns Job object
                '''
                response = self.async_api_rest.append_audio_url(body={ 'url': url }, conversation_id=conversation_id)
                print("Job with jobId " + response.job_id + " started!")

                if not wait:
                    job = Job(self.api_client, jobId=response.job_id, conversationId=response.conversation_id, wait=wait)
                    return function(job)

                job = Job(self.api_client, jobId=response.job_id, conversationId=response.conversation_id, wait=wait)
                return function(job.getConversationId())
            return wrapper()
        return inner

    def append_video_url(self, credentials=None, url : str = None, conversation_id:str = None, wait: bool = False):
        def inner(function):
            @self.initialize_api_client
            def wrapper(*args, **kw):
                '''
                    url of video file to be appended
                    returns Job object
                '''
                response = self.async_api_rest.append_video_url(body={ 'url': url }, conversationId=conversation_id)
                print("Job with jobId " + response.job_id + " started!")

                if not wait:
                    job = Job(self.api_client, jobId=response.job_id, conversationId=response.conversation_id, wait=wait)
                    return function(job)

                job = Job(self.api_client, jobId=response.job_id, conversationId=response.conversation_id, wait=wait)
                return function(job.getConversationId())
            return wrapper()
        return inner
