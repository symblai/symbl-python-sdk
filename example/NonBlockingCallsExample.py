import symbl

# A success callback to be triggered if Job is completed
def success_callback(conversation):
    print(conversation.get_messages())

# An error callback to be triggered if Job is Failed
def error_callback(conversation):
    print('job with jobId {0} has failed!'.format(conversation.job_id))

# Non blocking call to API to process audio file 
symbl.Audio.process_file(file_path="", wait=False).on_complete(success_callback).on_error(error_callback)

print("Continued Execution without a blocking call!")