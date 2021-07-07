# Non-blocking calls means that if an response can't be returned rapidly, the API returns immediately with an error and does nothing else 
# or returns response after the completion of the execution.
# so, in this code snippet we have defined functions for error and success response which will be called automatically by API

import symbl

# A success callback to be triggered if Job is completed
def success_callback(conversation_object):
    print(conversation_object.get_messages())

# An error callback to be triggered if Job is Failed
def error_callback(conversation_object):
    print('job with jobId {0} has failed!'.format(conversation_object.job_id))

# Non blocking call to API to process audio file 
symbl.Audio.process_file(file_path="<file_path>", wait=False).on_complete(success_callback).on_error(error_callback)

print("Continued Execution without a blocking call!")