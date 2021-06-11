from symbl.utils import wrap_keyboard_interrupt, Thread, Log
from symbl.utils.Helper import initialize_api_client
from symbl.jobs_api.JobStatus import JobStatus
from symbl_rest import JobsApi

import time

class Job():

    __INTERVAL_TIME_IN_SECONDS = 5  ## in seconds

    def __init__(self, job_id: str, conversation_id:str, wait=True):

        self.__job_id = job_id
        self.__conversation_id = conversation_id
        self.__success_func = None
        self.__jobs_api = JobsApi()
        self.__error_func = None
        self.__job_status = JobStatus.IN_PROGRESS
        self.__wait = wait

    def getConversationId(self):
        return self.__conversation_id

    def get_job_status(self):
        return self.__job_status.value

    def get_job_id(self):
        return self.__job_id

    def on_complete(self, func):
        self.__success_func = func
        return self

    def on_error(self, func):
        self.__error_func = func
        return self

    @initialize_api_client
    def __fetch_current_job_status(self, credentials=None):
        if self.__jobs_api is not None:
            response = self.__jobs_api.get_job_status(self.__job_id)
            self.__job_status = JobStatus(response.status)
        else:
            raise ValueError("Job object not initialized correctly. Please contact administrator.")

    def synchronous_monitor_job(self, conversation, interval=None, wait=True, credentials=None):
        if interval is None:
            interval = self.__INTERVAL_TIME_IN_SECONDS

        while self.__job_status != JobStatus.COMPLETED and self.__job_status != JobStatus.FAILED:
            time.sleep(interval)
            self.__fetch_current_job_status(credentials=credentials)
            Log.getInstance().info("Fetching latest status of job {0}, current status is {1}".format(self.__job_id, self.__job_status.value))

        if self.__job_status == JobStatus.COMPLETED and self.__success_func != None:
            self.__success_func(conversation)

        elif self.__error_func != None:
            self.__error_func(conversation)

    @wrap_keyboard_interrupt
    def monitor_job(self, conversation, interval=None, wait=True, credentials=None):
        if wait:
            self.synchronous_monitor_job(conversation, interval, wait, credentials)
        else:
            Thread.getInstance().start_on_thread(self.synchronous_monitor_job, conversation, interval, wait, credentials)
