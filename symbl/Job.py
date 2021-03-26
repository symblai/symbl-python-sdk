from symbl.JobStatus import JobStatus
import threading
from symbl_rest import JobsApi

class Job():

    INTERVAL_TIME_IN_SECONDS = 5  ## in seconds

    def __init__(self, api_client = None, jobId=None, conversationId:str=None, wait=True):
        if api_client is None:
            raise ValueError('Please initialize sdk with correct app_id and app_secret.')

        self.api_client = api_client
        self.job_id = jobId
        self.conversation_id = conversationId
        self.success_func = None
        self.error_func = None
        self.job_status = JobStatus.IN_PROGRESS
        self.wait = wait
        
        self.monitorJob(30, wait)
    
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
    
    def monitorJob(self, interval=None, wait=True):

        if interval is None:
            interval = self.INTERVAL_TIME_IN_SECONDS
        
        response = JobsApi(self.api_client).get_job_status(self.job_id)
        
        self.job_status = JobStatus(response.status)

        print("Fetching latest status of job {0}, current status is {1}".format(self.job_id, response.status))
        
        if JobStatus(response.status) != JobStatus.COMPLETED and JobStatus(response.status) != JobStatus.FAILED:
            timer = threading.Timer(interval, self.monitorJob, [30])
            timer.start()
            if wait == True:
                timer.join()
        
        elif(JobStatus(response.status) == JobStatus.COMPLETED):
            if self.success_func != None:
                self.success_func({'jobId': self.job_id, 'conversationId': self.conversation_id})

        elif self.error_func != None:
            self.error_func({'jobId': self.job_id, 'conversationId': self.conversation_id})