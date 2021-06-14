from symbl.jobs_api.Job import Job
from symbl.conversations_api.ConversationsApi import ConversationsApi
from symbl.utils.Logger import Log


def validate_conversation_id(function):
    def wrapper(*args, **kwargs):
        self = args[0]
        if self.get_conversation_id() != None:
            return function(*args, **kwargs)
        else:
            Log.getInstance().error("Conversation not initialized")
    return wrapper
class Conversation():

    __INTERVAL_TIME_IN_SECONDS = 30  ## in seconds

    def __init__(self, conversation_id: str, job_id: str=None,  wait=True, credentials=None):

        self.__conversation_id = conversation_id
        self.__wait = wait
        self.__credentials = credentials
        self.__conversation_api = ConversationsApi()

        if job_id != None:
            self.__job = Job(conversation_id=conversation_id, job_id=job_id, wait=wait)
            self.__job.monitor_job(self, interval=self.__INTERVAL_TIME_IN_SECONDS, wait=self.__wait, credentials=self.__credentials)
        else:
            self.__job = None
    
    def get_conversation_id(self):
        return self.__conversation_id
    
    def get_job_status(self):
        if self.__job != None:
            return self.__job.get_job_status()
        return None

    def get_job_id(self):
        if self.__job != None:
            return self.__job.get_job_id()
        return None

    def on_complete(self, func):
        self.__job.on_complete(func)
        return self

    def on_error(self, func):
        self.__job.on_error(func)
        return self

    @validate_conversation_id
    def get_action_items(self):
        return self.__conversation_api.get_action_items(self.__conversation_id, credentials=self.__credentials)

    @validate_conversation_id
    def get_follow_ups(self):
        return self.__conversation_api.get_follow_ups(self.__conversation_id, credentials=self.__credentials)
  
    @validate_conversation_id
    def get_members(self):  
        return self.__conversation_api.get_members(self.__conversation_id, credentials=self.__credentials)
  
    @validate_conversation_id
    def get_messages(self, parameters={}):
        return self.__conversation_api.get_messages(self.__conversation_id, credentials=self.__credentials, parameters=parameters)
  
    @validate_conversation_id
    def get_questions(self):  
        return self.__conversation_api.get_questions(self.__conversation_id, credentials=self.__credentials)
  
    @validate_conversation_id
    def get_topics(self, parameters={}):
        return self.__conversation_api.get_topics(self.__conversation_id, credentials=self.__credentials, parameters=parameters)