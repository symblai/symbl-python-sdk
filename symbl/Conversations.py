from symbl.jobs_api.Job import Job
from symbl.jobs_api.JobStatus import JobStatus
from symbl.conversations_api.ConversationsApi import ConversationsApi
from symbl_rest import JobsApi

class Conversation():

    __INTERVAL_TIME_IN_SECONDS = 30  ## in seconds

    def __init__(self, conversationId: str, jobId: str=None,  wait=True, credentials=None):
        
        self.__conversation_id = conversationId
        self.__wait = wait
        self.__credentials = credentials
        self.__conversation_api = ConversationsApi()

        if jobId != None:
            self.__job = Job(conversation_id=conversationId, job_id=jobId, wait=wait)
            self.__monitorJob()
    
    def get_conversation_id(self):
        return self.__conversation_id
    
    def get_job_status(self):
        return self.__job.__job_status.value

    def on_complete(self, func):
        self.__job.__success_func = func
        return self

    def on_error(self, func):
        self.__job.__error_func = func
        return self

    def action_items(self):
        return self.__conversation_api.get_action_items(self.__conversation_id, credentials=self.__credentials)

    def follow_ups(self):
        return self.__conversation_api.get_follow_ups(self.__conversation_id, credentials=self.__credentials)

    def insights(self):
        return self.__conversation_api.get_insights(self.__conversation_id, credentials=self.__credentials)
  
    def members(self):  
        return self.__conversation_api.get_members(self.__conversation_id, credentials=self.__credentials)
  
    def messages(self, parameters={}):  
        return self.__conversation_api.get_messages(self.__conversation_id, credentials=self.__credentials, parameters=parameters)
  
    def questions(self):  
        return self.__conversation_api.get_questions(self.__conversation_id, credentials=self.__credentials)
  
    def topics(self, parameters={}):  
        return self.__conversation_api.get_topics(self.__conversation_id, credentials=self.__credentials, parameters=parameters)
        
    def __monitorJob(self):
        self.__job.monitor_job(self, interval=self.__INTERVAL_TIME_IN_SECONDS, wait=self.__wait, credentials=self.__credentials)