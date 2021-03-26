import threading
from symbl_rest import AsyncApi as async_api_rest
from symbl.Job import Job

class AsyncApi():

    def __init__(self, api_client=None):
        '''
            It will initialize the Analysis class
            with the object of Initialize Class
        '''

        if api_client is None:
            raise ValueError('Please initialize sdk with correct app_id and app_secret.')
        
        self.api_client = api_client
        self.async_api_rest = async_api_rest(api_client)

    def submit_text(self, text_payload : dict = None, wait: bool = False):
        '''
            Text payload to be analyzed
            returns Job object
        '''

        response = self.async_api_rest.add_text(body=text_payload)
        print("Job with jobId " + response.job_id + " started!")

        if not wait:
            return Job(self.api_client, jobId=response.job_id, 
            conversationId=response.conversation_id, wait=wait)

        job = Job(self.api_client, jobId=response.job_id, conversationId=response.conversation_id, wait=wait)
        return job.getConversationId()

    def submit_audio(self, file_path:str = None, content_type:str='', wait:bool=True):
        '''
            audio files to be analyzed
            returns Job object
        '''
        file = open(file_path, 'rb')
        audio_file = file.read()
        response = self.async_api_rest.add_audio(body=audio_file, content_type=content_type)
        print("Job with jobId " + response.job_id + " started!")

        if not wait:
            return Job(self.api_client, jobId=response.job_id, 
            conversationId=response.conversation_id, wait=wait)

        job = Job(self.api_client, jobId=response.job_id, conversationId=response.conversation_id, wait=wait)
        return job.getConversationId()

    def submit_video(self, file_path:str = None, content_type:str='', wait:bool=True):
        '''
            video files to be analyzed
            returns Job object
        '''
        file = open(file_path, 'rb')
        audio_file = file.read()
        response = self.async_api_rest.add_audio(body=audio_file, content_type=content_type)
        print("Job with jobId " + response.job_id + " started!")

        if not wait:
            return Job(self.api_client, jobId=response.job_id, 
            conversationId=response.conversation_id, wait=wait)

        job = Job(self.api_client, jobId=response.job_id, conversationId=response.conversation_id, wait=wait)
        return job.getConversationId()
    
    def submit_audio_url(self, url : str = None, wait: bool = False):
        '''
            url of audio file to be analyzed
            returns Job object
        '''
        response = self.async_api_rest.add_audio_url(body={ 'url': url })
        print("Job with jobId " + response.job_id + " started!")

        if not wait:
            return Job(self.api_client, jobId=response.job_id, 
            conversationId=response.conversation_id, wait=wait)

        job = Job(self.api_client, jobId=response.job_id, conversationId=response.conversation_id, wait=wait)
        return job.getConversationId()

    def submit_video_url(self, url : str = None, wait: bool = False):
        '''
            url of audio file to be analyzed
            returns Job object
        '''

        response = self.async_api_rest.add_video_url(body={ 'url': url })
        print("Job with jobId " + response.job_id + " started!")

        if not wait:
            return Job(self.api_client, jobId=response.job_id, 
            conversationId=response.conversation_id, wait=wait)

        job = Job(self.api_client, jobId=response.job_id, conversationId=response.conversation_id, wait=wait)
        return job.getConversationId()

    def append_text(self, text_payload : dict = None, conversation_id:str = None, wait: bool = False):
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
            return Job(self.api_client, jobId=response.job_id, 
            conversationId=response.conversation_id, wait=wait)

        job = Job(self.api_client, jobId=response.job_id, conversationId=response.conversation_id, wait=wait)
        return job.getConversationId()

    def append_audio(self, file_path:str = None, conversation_id:str = None, content_type:str='', wait:bool=True):
        '''
            audio files to be appended
            returns Job object
        '''
        file = open(file_path, 'rb')
        audio_file = file.read()
        response = self.async_api_rest.append_audio(body=audio_file, content_type=content_type, conversationId= conversation_id)
        print("Job with jobId " + response.job_id + " started!")

        if not wait:
            return Job(self.api_client, jobId=response.job_id, 
            conversationId=response.conversation_id, wait=wait)

        job = Job(self.api_client, jobId=response.job_id, conversationId=response.conversation_id, wait=wait)
        return job.getConversationId()

    def append_video(self, file_path:str = None, conversation_id:str = None, content_type:str='', wait:bool=True):
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
            return Job(self.api_client, jobId=response.job_id, 
            conversationId=response.conversation_id, wait=wait)

        job = Job(self.api_client, jobId=response.job_id, conversationId=response.conversation_id, wait=wait)
        return job.getConversationId()
    
    def append_audio_url(self, url : str = None, conversation_id:str = None, wait: bool = False):
        '''
            url of audio file to be appended
            returns Job object
        '''
        response = self.async_api_rest.append_audio_url(body={ 'url': url }, conversation_id=conversation_id)
        print("Job with jobId " + response.job_id + " started!")

        if not wait:
            return Job(self.api_client, jobId=response.job_id, 
            conversationId=response.conversation_id, wait=wait)

        job = Job(self.api_client, jobId=response.job_id, conversationId=response.conversation_id, wait=wait)
        return job.getConversationId()

    def append_video_url(self, url : str = None, conversation_id:str = None, wait: bool = False):
        '''
            url of video file to be appended
            returns Job object
        '''
        response = self.async_api_rest.append_video_url(body={ 'url': url }, conversationId=conversation_id)
        print("Job with jobId " + response.job_id + " started!")

        if not wait:
            return Job(self.api_client, jobId=response.job_id, 
            conversationId=response.conversation_id, wait=wait)

        job = Job(self.api_client, jobId=response.job_id, conversationId=response.conversation_id, wait=wait)
        return job.getConversationId()
