from symbl.utils.Helper import dictionary_to_valid_json, correct_boolean_values, initialize_api_client
from symbl.utils.Logger import Log
from symbl.Conversations import Conversation
from symbl_rest import AsyncApi as async_api_rest

class Audio():

    def __init__(self):
        '''
            It will initialize the Analysis class
            with the object of Initialize Class
        '''
        self.__async_api_rest = async_api_rest()

    @initialize_api_client
    def process_file(self, file_path:str, credentials=None, content_type:str='', wait:bool=True, parameters={}):
        '''
            audio files to be analyzed
            returns Conversation object
        '''
        if file_path == None:
            raise ValueError("Please enter a valid file_path")
        
        params = dictionary_to_valid_json(parameters)

        file = open(file_path, 'rb')
        audio_file = file.read()
        response = self.__async_api_rest.add_audio(body=audio_file, content_type=content_type, **correct_boolean_values(params))
        Log.getInstance().info("Job with jobId {} for conversationId {} started".format(response.job_id, response.conversation_id))

        return Conversation(response.conversation_id, response.job_id, wait=wait, credentials=credentials)

    @initialize_api_client
    def process_url(self, payload:dict, credentials=None, wait:bool=True, parameters={}):
        '''
            url of audio file to be analyzed
            returns Conversation object
        '''

        if 'url' not in payload or payload['url'] == None:
            raise ValueError("Please enter a valid file_path")
        
        params = dictionary_to_valid_json(parameters)

        response = self.__async_api_rest.add_audio_url(body=payload, **correct_boolean_values(params))
        Log.getInstance().info("Job with jobId {} for conversationId {} started".format(response.job_id, response.conversation_id))

        return Conversation(response.conversation_id, response.job_id, wait=wait, credentials=credentials)
        

    @initialize_api_client
    def append_file(self, file_path:str, conversation_id:str, credentials=None, content_type:str='', wait:bool=True, parameters={}):
        '''
            audio files to be appended
            returns Conversation object
        '''
        if file_path == None:
            raise ValueError("Please enter a valid file_path")
        
        if conversation_id == None or len(conversation_id) == 0:
            raise ValueError("Please enter a valid conversation_id")
        
        params = dictionary_to_valid_json(parameters)

        file = open(file_path, 'rb')
        audio_file = file.read()
        response = self.__async_api_rest.append_audio(body=audio_file, content_type=content_type, conversation_id=conversation_id,  **correct_boolean_values(params))
        Log.getInstance().info("Job with jobId {} for conversationId {} started".format(response.job_id, response.conversation_id))

        return Conversation(response.conversation_id, response.job_id, wait=wait, credentials=credentials)
  
    @initialize_api_client  
    def append_url(self, payload:dict, conversation_id:str, credentials=None, wait:bool=True, parameters={}):
        '''
            url of audio file to be appended
            returns Conversation object
        '''
        if 'url' not in payload or payload['url'] == None:
            raise ValueError("Please enter a valid url")

        if conversation_id == None or len(conversation_id) == 0:
            raise ValueError("Please enter a valid conversationId")
        
        params = dictionary_to_valid_json(parameters)

        response = self.__async_api_rest.append_audio_url(body=payload, conversation_id=conversation_id,  **correct_boolean_values(params))
        Log.getInstance().info("Job with jobId {} for conversationId {} started".format(response.job_id, response.conversation_id))

        return Conversation(response.conversation_id, response.job_id, wait=wait, credentials=credentials)
