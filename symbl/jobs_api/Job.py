from symbl.AuthenticationToken import get_api_client
from symbl.jobs_api.JobStatus import JobStatus
import threading
from symbl_rest import JobsApi

class Job():

    INTERVAL_TIME_IN_SECONDS = 5  ## in seconds

    def __init__(self, jobId=None, conversationId:str=None, wait=True):

        self.job_id = jobId
        self.conversation_id = conversationId
        self.success_func = None
        self.error_func = None
        self.job_status = JobStatus.IN_PROGRESS
        self.wait = wait

    def initialize_api_client(function):
        def wrapper(*args, **kw):
            credentials = None
            self = args[0]
            
            if 'credentials' in kw:
                credentials = kw['credentials']

            api_client = get_api_client(credentials)
            self.api_client = api_client
            self.jobs_api = JobsApi(api_client)

            function(*args, **kw)
        
        return wrapper
    
    def getConversationId(self):
        return self.conversation_id
    
    def getJobStatus(self):
        return self.job_status.value

    def on_complete(self, func):
        self.success_func = func
        return self

    def on_error(self, func):
        self.error_func = func
        return self
    
    @initialize_api_client
    def monitorJob(self, conversation, interval=None, wait=True, credentials=None):
        if interval is None:
            interval = self.INTERVAL_TIME_IN_SECONDS
        
        response = self.jobs_api.get_job_status(self.job_id)
        
        self.job_status = JobStatus(response.status)

        print("Fetching latest status of job {0}, current status is {1}".format(self.job_id, response.status))
        
        if JobStatus(response.status) != JobStatus.COMPLETED and JobStatus(response.status) != JobStatus.FAILED:
            timer = threading.Timer(interval, self.monitorJob, [conversation, interval, wait, credentials])
            timer.start()
            if wait == True:
                timer.join()
        
        elif(JobStatus(response.status) == JobStatus.COMPLETED):
            if self.success_func != None:
                self.success_func(conversation)

        elif self.error_func != None:
            self.error_func(conversation)