# Symbl Python SDK

The Symbl Python sdk provides convenient access to the Symbl API from
applications written in the Python language. It includes a pre-defined set of
classes for a simple and clear utilization of APIs.


## Documentation

See the [Python API docs](https://docs.symbl.ai/docs/).


## Installation

You don't need this source code unless you want to modify the package. If you just
want to use the package, just run:

```sh
pip install --upgrade symbl
```

Install from source with:

```sh
python setup.py install
```

### Requirements

-   Python 2.7+ or Python 3.4+ (PyPy supported)

## Usage

The library needs to be configured with your account's credentials (appId & appSecret) which is
available in your [Symbl Dashboard][api-keys].

```python
import symbl

# Initialize with credentials
symbl.init(app_id=<app_id>, app_secret=<app_secret>)

# Process audio file
conversation_id = symbl.async_api.process_audio_file(file_path=<file_path>)

# Get Transcription as array of messages
transcription_messages = symbl.conversation_api.get_messages(conversation_id)
```

### Non Blocking calls to API with Callbacks

```python

import symbl

# Initialize with credentials
symbl.init(app_id=<app_id>, app_secret=<app_secret>)

# A success callback to be triggered if Job is completed
def success_callback(jobPayload):
    symbl.conversationApiClient.get_messages_by(conversation_id=jobPayload.conversation_id)

# An error callback to be triggered if Job is Failed
def error_callback(jobPayload):
    print('job with jobId {0} has failed!'.format(jobPayload.job_id))

# Non blocking call to API to process audio file 
job = symbl.async_api.process_audio_file(file_path=<file_path>, wait=False).on_success(success_callback).on_error(error_callback)

print("Continued Execution without a blocking call!")

```

### async_api class

Symbl's Async APIs provide the functionality for processing recordings (audio/video) from files 
or public/signed URLs or textual content from a conversation. The data processed for these 
conversations is available via the Conversation APIs once the APIs have completed the processing. 

You can utilize different functions of Async APIs by directly utilizing `symbl.async_api`

You can use the following methods to upload your files to symbl in order to get them processed.

1. submit_text(text_payload, wait=True):

    text_payload:- (Mandatory) textual dictionary containing the conversation to be processed in textual form, See [docs][symbl-docs] for payload 

    wait :- (Optional, by default True) Boolean, Value False will execute the function submit_text on a separate thread making it a non blocking API call (Has callback support)

2. submit_audio(file_path, content_type='', wait=True):

    audio_file :- (Mandatory) A valid path to a file

    content_type: (Optional) Parameter defining the content_type of audio. Acceptable values are audio/wav, audio/mp3, audio/mpeg. Leave it blank if you're not sure about the content_type of file

    wait :- (Optional, by default True) Boolean, Value False will execute the function submit_audio on a separate thread making it a non blocking API call (Has callback support)

3. submit_video(file_path, content_type='', wait=True):

    video_file :- (Mandatory) A valid path to a file

    content_type: (Optional) Parameter defining the content_type of video. Acceptable values are video/mp4. Leave it blank if you're not sure about the content_type of file

    wait :- (Optional, by default True) Boolean, Value False will execute the function submit_video on a separate thread making it a non blocking API call (Has callback support)

4. submit_audio_url(url, wait=True):
    url :- (Mandatory) A valid url to a file hosted directly

    wait :- (Optional, by default True) Boolean, Value False will execute the function submit_video on a separate thread making it a non blocking API call (Has callback support)

5. submit_video_url(url, wait=True):
    url :- (Mandatory) A valid url to a file hosted directly

    wait :- (Optional, by default True) Boolean, Value False will execute the function submit_video on a separate thread making it a non blocking API call (Has callback support)

6. append_text(text_payload, conversation_id='' wait=True):

    text_payload:- (Mandatory) textual dictionary containing the conversation to be processed in textual form, See [docs][symbl-docs] for payload 

    conversation_id:- (Mandatory) conversationId of a previous conversation to which appending the current conversation

    wait :- (Optional, by default True) Boolean, Value False will execute the function submit_text on a separate thread making it a non blocking API call (Has callback support)

7. append_audio(file_path, content_type='', conversation_id='', wait=True):

    audio_file :- (Mandatory) A valid path to a file

    content_type: (Optional) Parameter defining the content_type of audio. Acceptable values are audio/wav, audio/mp3, audio/mpeg. Leave it blank if you're not sure about the content_type of file 

    conversation_id:- (Mandatory) conversationId of a previous conversation to which appending the current conversation

    wait :- (Optional, by default True) Boolean, Value False will execute the function submit_audio on a separate thread making it a non blocking API call (Has callback support)

8. append_video(file_path, content_type='', conversation_id='', wait=True):

    video_file :- (Mandatory) A valid path to a file

    content_type: (Optional) Parameter defining the content_type of video. Acceptable values are video/mp4. Leave it blank if you're not sure about the content_type of file 

    conversation_id:- (Mandatory) conversationId of a previous conversation to which appending the current conversation

    wait :- (Optional, by default True) Boolean, Value False will execute the function submit_video on a separate thread making it a non blocking API call (Has callback support)

9. append_audio_url(url, conversation_id='', wait=True):
    url :- (Mandatory) A valid url to a file hosted directly 

    conversation_id:- (Mandatory) conversationId of a previous conversation to which appending the current conversation

    wait :- (Optional, by default True) Boolean, Value False will execute the function submit_video on a separate thread making it a non blocking API call (Has callback support)

10. append_video_url(url, conversation_id='', wait=True):
    url :- (Mandatory) A valid url to a file hosted directly 

    conversation_id:- (Mandatory) conversationId of a previous conversation to which appending the current conversation

    wait :- (Optional, by default True) Boolean, Value False will execute the function submit_video on a separate thread making it a non blocking API call (Has callback support)


### conversation_api class

The Conversation API provides a REST API interface for getting your processed Speech to Text data(also known as Transcripts) and conversational insights.

These APIs require a conversationId.

You can utilize different functions of Conversation APIs by directly utilizing `symbl.conversation_api`

1. get_action_items(conversation_id):

    returns An action item is a specific outcome recognized in the conversation that requires one or more people in the conversation to act in the future
  
2. get_follow_ups(conversation_id ):  

    return a category of action items with a connotation to follow-up a request or a task like sending an email or making a phone call or booking an appointment or setting up a meeting.

3. get_insights(conversation_id):  

    returns a list of objects containing information about each message along with it's type, confidence score, messageIds etc. 
        
4. get_members(conversation_id):  

    return a list of all the members in a conversation. A Member is referred to a participant in the conversation that is uniquely identified as a speaker. Identifying different participants in the meetings can be done by implementing speaker separation.
        
5. get_messages(conversation_id):  

    returns a list of all the messages in a conversation. You can use this for providing transcription for video conference, meeting or telephone call.
        
6. get_questions(conversation_id): 

    returns explicit question or request for information that comes up during the conversation, whether answered or not, is recognized as a question.
        
7. get_topics(conversation_id):  

    returs The most relevant topics of discussion from the conversation that are generated based on the combination of the overall scope of the discussion.


### Sample Code to pretty print all the messages

import symbl

symbl.init(app_id="", app_secret="")

conversation_id = symbl.async_api.submit_audio(file_path=file_path)

extract_text = lambda responses : [response.text for response in responses]
pretty_print = lambda text_array : [print(text) for text in text_array]

response = symbl.conversations_api.get_messages(conversation_id=conversation_id)

pretty_print(extract_text(response.messages))


[api-keys]: https://platform.symbl.ai/#/login
[symbl-docs]: https://docs.symbl.ai/docs/