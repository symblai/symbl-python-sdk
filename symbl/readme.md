
## Want to know more about SDK?

SDK offers easy implementation of multiple APIs provided by Symbl.

1. [Audio][audio_api-class]

2. [Video][video_api-class]

3. [Text][text_api-class]

4. [Conversation APIs][conversation_api-class]

5. [Telephony API][telephony_api-class]


## Key Terms
### What is a ConversationId?

When you process any conversation through Symbl whether it's from Async API, Javascript SDK, Telephony or Streaming API, you'll always receive a unique Conversation ID (conversationId), which consists of numerical digits.

### What is a JobId?

As soon as you upload one of your files, or send one of your text for processing to Symbl, You get a jobId (and a conversationId) in response. This jobId is a unique identifier for the job processing the payload you sent. 

A job can have a particular status at a time wiz. IN_PROGRESS, SCHEDULED, COMPLETED or FAILED. You can only use a conversationId for the conversation_api class functions once, the job payload is completed.

# audio_api class

Symbl's Async APIs provide the functionality for processing audio recordings from files or public/signed URLs. The data processed for these conversations are available via the Conversation APIs once the APIs have completed the processing. 

You can utilize different functions of Async APIs by directly utilizing `symbl.Audio`.

1. submit_audio(file_path, content_type='', wait=True):

    audio_file :- (Mandatory) A valid path to a file

    content_type: (Optional) Parameter defining the content_type of audio. Acceptable values are audio/wav, audio/mp3, audio/mpeg. Leave it blank if you're not sure about the content_type of file

    wait:- (Optional, by default True) Boolean, Value False will execute the function submit_audio on a separate thread making it a non-blocking API call (Has callback support)

    returns conversation object

2. submit_audio_url(url, wait=True):
    url :- (Mandatory) A valid url to a file hosted directly

    wait:- (Optional, by default True) Boolean, Value False will execute the function submit_video on a separate thread making it a non-blocking API call (Has callback support)

    returns conversation object

3. append_audio(file_path, content_type='', conversation_id='', wait=True):

    audio_file :- (Mandatory) A valid path to a file

    content_type: (Optional) Parameter defining the content_type of audio. Acceptable values are audio/wav, audio/mp3, audio/mpeg. Leave it blank if you're not sure about the content_type of file 

    conversation_id:- (Mandatory) conversationId of a previous conversation to which appending the current conversation

    wait:- (Optional, by default True) Boolean, Value False will execute the function submit_audio on a separate thread making it a non-blocking API call (Has callback support)

    returns conversation object

4. append_audio_url(url, conversation_id='', wait=True):
    url :- (Mandatory) A valid url to a file hosted directly 

    conversation_id:- (Mandatory) conversationId of a previous conversation to which appending the current conversation

    wait:- (Optional, by default True) Boolean, Value False will execute the function submit_video on a separate thread making it a non-blocking API call (Has callback support)

    returns conversation object

# video_api class

Symbl's Async APIs provide the functionality for processing video recordings from files or public/signed URLs. The data processed for these conversations are available via the Conversation APIs once the APIs have completed the processing. 

You can utilize different functions of Async APIs by directly utilizing `symbl.Video`.


1. submit_video(file_path, content_type='', wait=True):

    video_file :- (Mandatory) A valid path to a file

    content_type: (Optional) Parameter defining the content_type of video. Acceptable values are video/mp4. Leave it blank if you're not sure about the content_type of file

    wait:- (Optional, by default True) Boolean, Value False will execute the function submit_video on a separate thread making it a non-blocking API call (Has callback support)

    returns conversation object

2. submit_video_url(url, wait=True):
    url:- (Mandatory) A valid url to a file hosted directly

    wait:- (Optional, by default True) Boolean, Value False will execute the function submit_video on a separate thread making it a non-blocking API call (Has callback support)

    returns conversation object

3. append_video(file_path, content_type='', conversation_id='', wait=True):

    video_file :- (Mandatory) A valid path to a file

    content_type: (Optional) Parameter defining the content_type of video. Acceptable values are video/mp4. Leave it blank if you're not sure about the content_type of file 

    conversation_id:- (Mandatory) conversationId of a previous conversation to which appending the current conversation

    wait:- (Optional, by default True) Boolean, Value False will execute the function submit_video on a separate thread making it a non-blocking API call (Has callback support)

    returns conversation object

4. append_video_url(url, conversation_id='', wait=True):
    url :- (Mandatory) A valid url to a file hosted directly 

    conversation_id:- (Mandatory) conversationId of a previous conversation to which appending the current conversation

    wait:- (Optional, by default True) Boolean, Value False will execute the function submit_video on a separate thread making it a non-blocking API call (Has callback support)

    returns conversation object

# text_api class

Symbl's Async APIs provide the functionality for processing textual content from a conversation. The data processed for these conversations are available via the Conversation APIs once the APIs have completed the processing. 

You can utilize different functions of Async APIs by directly utilizing `symbl.Text`.

1. submit_text(text_payload, wait=True):

    text_payload:- (Mandatory) textual dictionary containing the conversation to be processed in textual form, See [docs][symbl-docs] for payload 

    wait:- (Optional, by default True) Boolean, Value False will execute the function submit_text on a separate thread making it a non-blocking API call (Has callback support)

    returns conversation object

2. append_text(text_payload, conversation_id='' wait=True):

    text_payload:- (Mandatory) textual dictionary containing the conversation to be processed in textual form, See [docs][symbl-docs] for payload 

    conversation_id:- (Mandatory) conversationId of a previous conversation to which appending the current conversation

    wait:- (Optional, by default True) Boolean, Value False will execute the function submit_text on a separate thread making it a non-blocking API call (Has callback support)

    returns conversation object

## conversation object

Conversation object is returned by Async API Text, Audio and Video classes. The conversation object is a shorthand for conversation API and can be utilized for fetching multiple insights.

1. conversation.action_items(): returns Action Items which are some specific outcomes recognized in the conversation that requires one or more people in the conversation to act in the future
  
2. conversation.follow_ups(): return a category of action items with a connotation to follow-up a request or a task like sending an email or making a phone call or booking an appointment or setting up a meeting.
        
3. conversation.members(): return a list of all the members in a conversation. A Member is referred to as a participant in the conversation that is uniquely identified as a speaker. Identifying different participants in the meetings can be done by implementing speaker separation.
        
4. conversation.messages(): returns a list of messages (sentences spoken by speakers) in a conversation. You can use this for providing transcription for video conference, meeting or telephone call.
 
5. conversation.questions(): returns explicit question or request for information that comes up during the conversation, whether answered or not, is recognized as a question.
 
6. conversation.topics(): returns The most relevant topics of discussion from the conversation that is generated based on the combination of the overall scope of the discussion.


# conversation_api class

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

# telephony_api class

Based on PSTN and SIP protocols, the Telephony API provides an interface for the developers to have Symbl bridge/join VoIP calls and get the results back in real-time as well. Optionally, the developer can also trigger an email at the end of the conversation containing the URL to view the transcription, insights and topics in a single page Web Application.

1. start_pstn(phoneNumber, dtmf, actions, data):

    The body object needs to be in format.

    i.   phoneNumber: phoneNumber where symbl should call
    ii.  dtmf : (Optional) dtmf sequence to entered by symbl to join the call 
    iii. actions : (Optional) [{invokeOn: "stop", name: "sendSummaryEmail", parameters: {emails: ["email@example.com"]}}]
    iv.  data: (Optional) {session: {name: "sessionName"}}
   
    For more details check documentation [here][telephony-docs]

    Returns a connection object

2. start_sip(uri, audioConfig, actions, data):

    The body object needs to be in format.

    i.   uri: uri where symbl should connect
    ii.  audioConfig : (Optional) audioConfigs of the SIP  
    iii. actions : (Optional) [{invokeOn: "stop", name: "sendSummaryEmail", parameters: {emails: ["email@example.com"]}}]
    iv.  data: (Optional) {session: {name: "sessionName"}}
   
    For more details check documentation [here][telephony-docs]

    Returns a connection object

3. stop(connectionId):

    Only connectionId parameter is required. Other optional parameters can be added as per [docs][telephony-docs]

    Return an updated connection object which will have the conversationId in the response. 


## connection object

The connection object is returned by telephony API's functions. A connection object can be utilized for subscribing to multiple insights using subscribe function and can also be used to stop the telephony connection.

1. connection.subscribe({'event': callback, ...}):
    
    takes a dictionary parameter, where the key can be an event and it's value can be a callback function that should be executed on the occurrence of that event.

2. connection.stop():

    used to stop the telephony connection.


[api-keys]: https://platform.symbl.ai/#/login
[symbl-docs]: https://docs.symbl.ai/docs/
[telephony-docs]: https://docs.symbl.ai/docs/telephony/introduction
[async_api-class]: https://github.com/symblai/symbl-python/blob/main/symbl/readme.md#async_api-class
[audio_api-class]: https://github.com/symblai/symbl-python/blob/main/symbl/readme.md#audio_api-class
[video_api-class]: https://github.com/symblai/symbl-python/blob/main/symbl/readme.md#video_api-class
[text_api-class]: https://github.com/symblai/symbl-python/blob/main/symbl/readme.md#text_api-class
[conversation_api-class]: https://github.com/symblai/symbl-python/blob/main/symbl/readme.md#conversation_api-class
[telephony_api-class]: https://github.com/symblai/symbl-python/blob/main/symbl/readme.md#telephony_api-class
[streaming_api-class]: https://github.com/symblai/symbl-python/blob/main/symbl/readme.md#telephony_api-class