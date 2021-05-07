from symbl.jobs_api.Job import Job
from symbl.jobs_api.JobStatus import JobStatus
from symbl.conversations_api.ConversationsApi import ConversationsApi
from symbl_rest import JobsApi

class Conversation():

    INTERVAL_TIME_IN_SECONDS = 30  ## in seconds

    def __init__(self, conversationId: str, jobId: str,  wait=True, credentials=None):
        
        self.conversation_id = conversationId
        self.job = Job(conversationId=conversationId, jobId=jobId, wait=wait)
        self.wait = wait
        self.credentials = credentials
        self.conversation_api = ConversationsApi()
        
        self.monitorJob()
    
    def getConversationId(self):
        return self.conversation_id
    
    def getJobStatus(self):
        return self.job.job_status.value

    def on_complete(self, func):
        self.job.success_func = func
        return self

    def on_error(self, func):
        self.job.error_func = func
        return self


    def action_items(self):
        return self.conversation_api.get_action_items(self.conversation_id, credentials=self.credentials)

    def follow_ups(self ):  
        return self.conversation_api.get_follow_ups(self.conversation_id, credentials=self.credentials)

    def insights(self):  
        return self.conversation_api.get_insights(self.conversation_id, credentials=self.credentials)
  
    def members(self):  
        return self.conversation_api.get_members(self.conversation_id, credentials=self.credentials)
  
    def messages(self):  
        return self.conversation_api.get_messages(self.conversation_id, credentials=self.credentials)
  
    def questions(self):  
        return self.conversation_api.get_questions(self.conversation_id, credentials=self.credentials)
  
    def topics(self):  
        return self.conversation_api.get_topics(self.conversation_id, credentials=self.credentials)
    
    def monitorJob(self):
        self.job.monitorJob(self, interval=self.INTERVAL_TIME_IN_SECONDS, wait=self.wait, credentials=self.credentials)