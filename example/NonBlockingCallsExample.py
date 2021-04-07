import symbl

# Initialize with credentials
symbl.init(app_id="", app_secret="")

# A success callback to be triggered if Job is completed
def success_callback(jobPayload):
    symbl.conversationApiClient.get_messages_by(conversation_id=jobPayload.conversation_id)

# An error callback to be triggered if Job is Failed
def error_callback(jobPayload):
    print('job with jobId {0} has failed!'.format(jobPayload.job_id))

# Non blocking call to API to process audio file 
job = symbl.async_api.process_audio_file(file_path="", wait=False).on_success(success_callback).on_error(error_callback)

print("Continued Execution without a blocking call!")