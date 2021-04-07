
#### Want to know more about SDK?

Symbl's Python SDK offers easy implementation of multiple APIs.

1. [Async APIs] [#async_api-class]

2. [Conversation APIs][#conversation_api-class]

For Audio/Video files, you can either directly submit the file from your system or you can pass a URL (where the files are directly hosted) to async_api functions as mentioned [here][#async_api-class].

### What is a Job?

As soon as you upload one of your file, or send one of your text for processing to Symbl, You get a jobId (and a conversationId) in response. This jobId is a unique identifier for the job processing the payload you sent. 

A job can have a particular status at a time wiz. IN_PROGRESS, SCHEDULED, COMPLETED or FAILED. You can only use a conversationId for the conversation_api class functions once, the job payload is completed.


### async_api class

Symbl's Async APIs provide the functionality for processing recordings (audio/video) from files or public/signed URLs or textual content from a conversation. The data processed for these conversations are available via the Conversation APIs once the APIs have completed the processing. 

You can utilize different functions of Async APIs by directly utilizing `symbl.async_api`.


1. submit_text(text_payload, wait=True):

    text_payload:- (Mandatory) textual dictionary containing the conversation to be processed in textual form, See [docs][symbl-docs] for payload 

    wait:- (Optional, by default True) Boolean, Value False will execute the function submit_text on a separate thread making it a non-blocking API call (Has callback support)

2. submit_audio(file_path, content_type='', wait=True):

    audio_file :- (Mandatory) A valid path to a file

    content_type: (Optional) Parameter defining the content_type of audio. Acceptable values are audio/wav, audio/mp3, audio/mpeg. Leave it blank if you're not sure about the content_type of file

    wait:- (Optional, by default True) Boolean, Value False will execute the function submit_audio on a separate thread making it a non-blocking API call (Has callback support)

3. submit_video(file_path, content_type='', wait=True):

    video_file :- (Mandatory) A valid path to a file

    content_type: (Optional) Parameter defining the content_type of video. Acceptable values are video/mp4. Leave it blank if you're not sure about the content_type of file

    wait:- (Optional, by default True) Boolean, Value False will execute the function submit_video on a separate thread making it a non-blocking API call (Has callback support)

4. submit_audio_url(url, wait=True):
    url :- (Mandatory) A valid url to a file hosted directly

    wait:- (Optional, by default True) Boolean, Value False will execute the function submit_video on a separate thread making it a non-blocking API call (Has callback support)

5. submit_video_url(url, wait=True):
    url:- (Mandatory) A valid url to a file hosted directly

    wait:- (Optional, by default True) Boolean, Value False will execute the function submit_video on a separate thread making it a non-blocking API call (Has callback support)

6. append_text(text_payload, conversation_id='' wait=True):

    text_payload:- (Mandatory) textual dictionary containing the conversation to be processed in textual form, See [docs][symbl-docs] for payload 

    conversation_id:- (Mandatory) conversationId of a previous conversation to which appending the current conversation

    wait:- (Optional, by default True) Boolean, Value False will execute the function submit_text on a separate thread making it a non-blocking API call (Has callback support)

7. append_audio(file_path, content_type='', conversation_id='', wait=True):

    audio_file :- (Mandatory) A valid path to a file

    content_type: (Optional) Parameter defining the content_type of audio. Acceptable values are audio/wav, audio/mp3, audio/mpeg. Leave it blank if you're not sure about the content_type of file 

    conversation_id:- (Mandatory) conversationId of a previous conversation to which appending the current conversation

    wait:- (Optional, by default True) Boolean, Value False will execute the function submit_audio on a separate thread making it a non-blocking API call (Has callback support)

8. append_video(file_path, content_type='', conversation_id='', wait=True):

    video_file :- (Mandatory) A valid path to a file

    content_type: (Optional) Parameter defining the content_type of video. Acceptable values are video/mp4. Leave it blank if you're not sure about the content_type of file 

    conversation_id:- (Mandatory) conversationId of a previous conversation to which appending the current conversation

    wait:- (Optional, by default True) Boolean, Value False will execute the function submit_video on a separate thread making it a non-blocking API call (Has callback support)

9. append_audio_url(url, conversation_id='', wait=True):
    url :- (Mandatory) A valid url to a file hosted directly 

    conversation_id:- (Mandatory) conversationId of a previous conversation to which appending the current conversation

    wait:- (Optional, by default True) Boolean, Value False will execute the function submit_video on a separate thread making it a non-blocking API call (Has callback support)

10. append_video_url(url, conversation_id='', wait=True):
    url :- (Mandatory) A valid url to a file hosted directly 

    conversation_id:- (Mandatory) conversationId of a previous conversation to which appending the current conversation

    wait:- (Optional, by default True) Boolean, Value False will execute the function submit_video on a separate thread making it a non-blocking API call (Has callback support)


### conversation_api class

The Conversation API provides a REST API interface for getting your processed Speech to Text data(also known as Transcripts) and conversational insights.

These APIs require a conversationId.

You can utilize different functions of Conversation APIs by directly utilizing `symbl.conversation_api`

1. get_action_items(conversation_id):

    returns Action Items which are some specific outcomes recognized in the conversation that requires one or more people in the conversation to act in the future
  
2. get_follow_ups(conversation_id):  

    return a category of action items with a connotation to follow-up a request or a task like sending an email or making a phone call or booking an appointment or setting up a meeting.
        
3. get_members(conversation_id):  

    return a list of all the members in a conversation. A Member is referred to a participant in the conversation that is uniquely identified as a speaker. Identifying different participants in the meetings can be done by implementing speaker separation.
        
4. get_messages(conversation_id):  

    returns a list of messages (sentences spoken by speakers) in a conversation. You can use this for providing transcription for video conference, meeting or telephone call.
        
5. get_questions(conversation_id): 

    returns explicit question or request for information that comes up during the conversation, whether answered or not, is recognized as a question.
        
6. get_topics(conversation_id):

    returns The most relevant topics of discussion from the conversation that is generated based on the combination of the overall scope of the discussion.

[api-keys]: https://platform.symbl.ai/#/login
[symbl-docs]: https://docs.symbl.ai/docs/