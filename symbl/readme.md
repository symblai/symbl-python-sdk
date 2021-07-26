
# Want to know more about SDK?

SDK offers easy implementation of multiple APIs provided by Symbl.

1. [Audio][audio_api-class]

2. [Video][video_api-class]

3. [Text][text_api-class]

4. [Conversation API][conversation_api-class]

5. [Telephony API][telephony_api-class]

6. [Streaming API][streaming_api-class]

# Key Terms

**What is a ConversationId?**
>
>When you process any conversation through Symbl whether it's from Async API, Javascript SDK, Telephony or Streaming API, you'll always receive a unique Conversation ID (conversationId), which consists of numerical digits.
>

**What is a JobId?**

>As soon as you upload one of your files, or send one of your text for processing to Symbl, You get a jobId (and a conversationId) in response. This jobId is a unique identifier for the job processing the payload you sent.
>
>A job can have a particular status at a time wiz. IN_PROGRESS, SCHEDULED, COMPLETED or FAILED. You can only use a conversationId for the conversation_api class functions once, the job payload is completed.

# Audio class

Symbl's Async APIs provide the functionality for processing audio recordings from files or public/signed URLs. The data processed for these conversations are available via the Conversation APIs once the APIs have completed the processing.  

You can utilize different functions of Async APIs by directly utilizing `symbl.Audio`.

1. process_file(file_path):
    >Parameter Name | Required | Value
    >--- | --- | ---
    >file_path | Mandatory | A valid path to a file
    >credentials | optional | Don't add this parameter if you have `symbl.conf` file in your home directory or working directory
    >content_type | optional | Parameter defining the content_type of audio. Acceptable values are [`audio/wav`, `audio/mp3`, `audio/mpeg`]. Leave it blank if you're not sure about the content_type of file
    >wait | optional |  (by default True) Boolean, Value `False` will execute the function submit_audio on a separate thread making it a non-blocking API call (Has callback support)
    >parameters | optional | (by default {}) Dictionary, Any parameter and it's value can be provided in the dictionary format. For getting a list of value check [here](https://docs.symbl.ai/docs/async-api/overview/audio/post-audio#query-params)
    
    >returns conversation object
    >
    >click [here](https://github.com/symblai/symbl-python/tree/main/example/Async_API/Audio_API/process_audio_file.py) to check the example for usage of parameters/arguments and conversation object

2. process_url(payload):
    >Parameter Name | Required | Value
    >--- | --- | ---
    >payload | Mandatory | A valid payload having `url` as the member and it should be valid to a file hosted directly. valid payload [`payload = { 'url': "<url>" }`]
    >credentials | optional | Don't add this parameter if you have `symbl.conf` file in your home directory or working directory
    >wait | optional |  (by default True) Boolean, Value `False` will execute the function submit_audio on a separate thread making it a non-blocking API call (Has callback support)
    >parameters | optional | (by default {}) Dictionary, Any parameter and it's value can be provided in the dictionary format. For getting a list of value check [here](https://docs.symbl.ai/docs/async-api/overview/audio/post-audio-url#query-params)
    
    >returns conversation object
    >
    >click [here](https://github.com/symblai/symbl-python/tree/main/example/Async_API/Audio_API/process_audio_url.py) to check the example for usage of parameters/arguments and conversation object

3. append_file(file_path, conversation_id):
    >Parameter Name | Required | Value
    >--- | --- | ---
    >file_path | Mandatory | A valid path to a file
    >conversation_id | Mandatory | conversationId of a previous conversation to which appending the current conversation
    >credentials | optional | Don't add this parameter if you have `symbl.conf` file in your home directory or working directory
    >content_type | optional | Parameter defining the content_type of audio. Acceptable values are [`audio/wav`, `audio/mp3`, `audio/mpeg`]. Leave it blank if you're not sure about the content_type of file
    >wait | optional |  (by default True) Boolean, Value `False` will execute the function submit_audio on a separate thread making it a non-blocking API call (Has callback support)
    >parameters | optional | (by default {}) Dictionary, Any parameter and it's value can be provided in the dictionary format. For getting a list of value check [here](https://docs.symbl.ai/docs/async-api/overview/audio/put-audio#query-params)
    
    >returns conversation object
    >
    >click [here](https://github.com/symblai/symbl-python/tree/main/example/Async_API/Audio_API/append_audio_file.py) to check the example for usage of parameters/arguments and conversation object

4. append_url(payload, conversation_id):
    >Parameter Name | Required | Value
    >--- | --- | ---
    >payload | Mandatory | A valid payload having `url` as the member and it should be valid to a file hosted directly. valid payload [`payload = { 'url': "<url>" }`]
    >conversation_id | Mandatory | conversationId of a previous conversation to which appending the current conversation
    >credentials | optional | Don't add this parameter if you have `symbl.conf` file in your home directory or working directory
    >wait | optional |  (by default True) Boolean, Value `False` will execute the function submit_audio on a separate thread making it a non-blocking API call (Has callback support)
    >parameters | optional | (by default {}) Dictionary, Any parameter and it's value can be provided in the dictionary format. For getting a list of value check [here](https://docs.symbl.ai/docs/async-api/overview/audio/put-audio-url#query-params)
    
    >returns conversation object
    >
    >click [here](https://github.com/symblai/symbl-python/tree/main/example/Async_API/Audio_API/append_audio_url.py) to check the example for usage of parameters/arguments and conversation object

# Video class

Symbl's Async APIs provide the functionality for processing video recordings from files or public/signed URLs. The data processed for these conversations are available via the Conversation APIs once the APIs have completed the processing.

You can utilize different functions of Async APIs by directly utilizing `symbl.Video`.

1. process_file(file_path):
    >Parameter Name | Required | Value
    >--- | --- | ---
    >file_path | Mandatory | A valid path to a file
    >credentials | optional | Don't add this parameter if you have `symbl.conf` file in your home directory or working directory
    >content_type | optional | Parameter defining the content_type of video. Acceptable values is [`video/mp4`]. Leave it blank if you're not sure about the content_type of file
    >wait | optional |  (by default True) Boolean, Value `False` will execute the function submit_video on a separate thread making it a non-blocking API call (Has callback support)
    >parameters | optional | (by default {}) Dictionary, Any parameter and it's value can be provided in the dictionary format. For getting a list of value check [here](https://docs.symbl.ai/docs/async-api/overview/video/post-video#query-params)
    
    >returns conversation object
    >
    >click [here](https://github.com/symblai/symbl-python/tree/main/example/Async_API/Video_API/process_video_file.py) to check the example for usage of parameters/arguments and conversation object

2. process_url(payload):
    >Parameter Name | Required | Value
    >--- | --- | ---
    >payload | Mandatory | A valid payload having `url` as the member and it should be valid to a file hosted directly. valid payload [`payload = { 'url': "<url>" }`]
    >credentials | optional | Don't add this parameter if you have `symbl.conf` file in your home directory or working directory
    >wait | optional |  (by default True) Boolean, Value `False` will execute the function submit_video on a separate thread making it a non-blocking API call (Has callback support)
    >parameters | optional | (by default {}) Dictionary, Any parameter and it's value can be provided in the dictionary format. For getting a list of value check [here](https://docs.symbl.ai/docs/async-api/overview/video/post-video-url#query-params)
    
    >returns conversation object
    >
    >click [here](https://github.com/symblai/symbl-python/tree/main/example/Async_API/Video_API/process_video_url.py) to check the example for usage of parameters/arguments and conversation object

3. append_file(file_path, conversation_id):
    >Parameter Name | Required | Value
    >--- | --- | ---
    >file_path | Mandatory | A valid path to a file
    >conversation_id | Mandatory | conversationId of a previous conversation to which appending the current conversation
    >credentials | optional | Don't add this parameter if you have `symbl.conf` file in your home directory or working directory
    >content_type | optional | Parameter defining the content_type of video. Acceptable values is [`application/json`]. Leave it blank if you're not sure about the content_type of file
    >wait | optional |  (by default True) Boolean, Value `False` will execute the function submit_video on a separate thread making it a non-blocking API call (Has callback support)
    >parameters | optional | (by default {}) Dictionary, Any parameter and it's value can be provided in the dictionary format. For getting a list of value check [here](https://docs.symbl.ai/docs/async-api/overview/video/put-video#query-params)
    
    >returns conversation object
    >
    >click [here](https://github.com/symblai/symbl-python/tree/main/example/Async_API/Video_API/append_video_file.py) to check the example for usage of parameters/arguments and conversation object

4. append_url(payload, conversation_id):
    >Parameter Name | Required | Value
    >--- | --- | ---
    >payload | Mandatory | A valid payload having `url` as the member and it should be valid to a file hosted directly. valid payload [`payload = { 'url': "<url>" }`]
    >conversation_id | Mandatory | conversationId of a previous conversation to which appending the current conversation
    >credentials | optional | Don't add this parameter if you have `symbl.conf` file in your home directory or working directory
    >wait | optional |  (by default True) Boolean, Value `False` will execute the function submit_video on a separate thread making it a non-blocking API call (Has callback support)
    >parameters | optional | (by default {}) Dictionary, Any parameter and it's value can be provided in the dictionary format. For getting a list of value check [here](https://docs.symbl.ai/docs/async-api/overview/video/put-video-url#query-params)
    
    >returns conversation object
    >
    >click [here](https://github.com/symblai/symbl-python/tree/main/example/Async_API/Video_API/append_video_url.py) to check the example for usage of parameters/arguments and conversation object

# Text class

Symbl's Async APIs provide the functionality for processing textual content from a conversation. The data processed for these conversations are available via the Conversation APIs once the APIs have completed the processing.

You can utilize different functions of Async APIs by directly utilizing `symbl.Text`.

1. process(payload):
    >Parameter Name | Required | Value
    >--- | --- | ---
    >payload | Mandatory | textual dictionary containing the conversation to be processed in textual form, valid payload `payload={"messages": [{"payload": {"content": "Hi Anthony. I saw your complaints about bad call reception on your mobile phone. Can I know what issues you are currently facing?"},"from": {"userId": "surbhi@example.com", "name": "Surbhi Rathore"}}]}`. See [docs][text_payload-docs] for payload
    >credentials | optional | Don't add this parameter if you have `symbl.conf` file in your home directory or working directory
    >content_type | optional | Parameter defining the content_type of video. Acceptable values is [`video/mp4`]. Leave it blank if you're not sure about the content_type of file
    >wait | optional |  (by default True) Boolean, Value `False` will execute the function submit_text on a separate thread making it a non-blocking API call (Has callback support)
    >parameters | optional | (by default {}) Dictionary, Any parameter and it's value can be provided in the dictionary format. For getting a list of value check [here](https://docs.symbl.ai/docs/async-api/overview/video/post-video#query-params)
    
    >returns conversation object
    >
    >click [here](https://github.com/symblai/symbl-python/tree/main/example/Async_API/Text_API/process_text.py) to check the example for usage of parameters/arguments and conversation object

2. append(payload, conversation_id):
    >Parameter Name | Required | Value
    >--- | --- | ---
    >payload | Mandatory | textual dictionary containing the conversation to be processed in textual form, valid payload `payload={"messages": [{"payload": {"content": "Hi Anthony. I saw your complaints about bad call reception on your mobile phone. Can I know what issues you are currently facing?"},"from": {"userId": "surbhi@example.com", "name": "Surbhi Rathore"}}]}`. See [docs][text_payload-docs] for payload
    >conversation_id | Mandatory | conversationId of a previous conversation to which appending the current conversation
    >credentials | optional | Don't add this parameter if you have `symbl.conf` file in your home directory or working directory
    >wait | optional |  (by default True) Boolean, Value `False` will execute the function submit_text on a separate thread making it a non-blocking API call (Has callback support)
    >parameters | optional | (by default {}) Dictionary, Any parameter and it's value can be provided in the dictionary format. For getting a list of value check [here](https://docs.symbl.ai/docs/async-api/overview/text/put-text#query-params)
    
    >returns conversation object
    >
    >click [here](https://github.com/symblai/symbl-python/tree/main/example/Async_API/Text_API/append_text.py) to check the example for usage of parameters/arguments and conversation object

## conversation object

Conversation object is returned by Async API Text, Audio and Video classes. The conversation object is a shorthand for conversation API and can be utilized for fetching multiple insights.

1. conversation.get_action_items():

    >returns Action Items which are some specific outcomes recognized in the conversation that requires one or more people in the conversation to act in the future
  
2. conversation.get_follow_ups():

    >returns a category of action items with a connotation to follow-up a request or a task like sending an email or making a phone call or booking an appointment or setting up a meeting.

3. conversation.get_members():

    >returns a list of all the members in a conversation. A Member is referred to as a participant in the conversation that is uniquely identified as a speaker. Identifying different participants in the meetings can be done by implementing speaker separation.

4. conversation.get_messages():

    >parameters:- (Optional) dictionary, takes a dictionary of parameters. For list of parameters accepted, please click [here](https://docs.symbl.ai/docs/conversation-api/messages#query-params)
    >
    >returns a list of messages (sentences spoken by speakers) in a conversation. You can use this for providing transcription for video conference, meeting or telephone call.

5. conversation.get_questions():

    >returns explicit question or request for information that comes up during the conversation, whether answered or not, is recognized as a question.

6. conversation.get_topics():

    >parameters:- (Optional) dictionary, takes a dictionary of parameters. For list of parameters accepted, please click [here](https://docs.symbl.ai/docs/conversation-api/get-topics#query-params)
    >
    >returns The most relevant topics of discussion from the conversation that is generated based on the combination of the overall scope of the discussion.

7. conversation.get_conversation():

    >returns the conversation meta-data like meeting name, member name and email, start and end time of the meeting, meeting type and meeting id.

8. conversation.get_entities(conversation_id)

    >provides a functionality to extract entities(custom, location, person, date, number, organization,datetime,daterange, etc ) from the conversation.

9. conversation.get_trackers(conversation_id)

    >returns the occurrence of certain key words or phrases from the conversation.

10. conversation.get_analytics(conversation_id)

    >returns the speaker ratio, talk time, silence, pace and overlap from the conversation.

>
>example for demonstrate the use of conversation class
>
```
import symbl

file = "<file_path>"
conversation_object = symbl.Audio.process_file(file_path=file)

print(conversation_object.get_messages())
print(conversation_object.get_action_items())
print(conversation_object.get_follow_ups())
print(conversation_object.get_members())
print(conversation_object.get_topics())
print(conversation_object.get_questions())
print(conversation_object.get_conversation())
print(conversation_object.get_analytics())
print(conversation_object.get_entities())
print(conversation_object.get_trackers())
```
# Conversations class

The Conversation API provides a REST API interface for getting your processed Speech to Text data(also known as Transcripts) and conversational insights.

These APIs require a conversationId.

You can utilize different functions of Conversation APIs by directly utilizing `symbl.Conversations`

1. get_action_items(conversation_id):

    >returns Action Items which are some specific outcomes recognized in the conversation that requires one or more people in the conversation to act in the future
  
2. get_follow_ups(conversation_id):  

    >returns a category of action items with a connotation to follow-up a request or a task like sending an email or making a phone call or booking an appointment or setting up a meeting.

3. get_members(conversation_id):  

    >returns a list of all the members in a conversation. A Member is referred to a participant in the conversation that is uniquely identified as a speaker. Identifying different participants in the meetings can be done by implementing speaker separation.

4. get_messages(conversation_id):  

    >parameters:- (Optional) dictionary, takes a dictionary of parameters. For list of parameters accepted, please click [here](https://docs.symbl.ai/docs/conversation-api/messages#query-params)
    >
    >returns a list of messages (sentences spoken by speakers) in a conversation. You can use this for providing transcription for video conference, meeting or telephone call.

5. get_questions(conversation_id):

    >returns explicit question or request for information that comes up during the conversation, whether answered or not, is recognized as a question.

6. get_topics(conversation_id):

    >parameters:- (Optional) dictionary, takes a dictionary of parameters. For list of parameters accepted, please click [here](https://docs.symbl.ai/docs/conversation-api/get-topics#query-params)
    >
    >returns The most relevant topics of discussion from the conversation that is generated based on the combination of the overall scope of the discussion.

7. get_conversation(conversation_id)

    >returns the conversation meta-data like meeting name, member name and email, start and end time of the meeting, meeting type and meeting id.

8. get_entities(conversation_id)

    >provides a functionality to extract entities(custom, location, person, date, number, organization,datetime,daterange, etc ) from the conversation.

9. get_trackers(conversation_id)

    >returns the occurrence of certain key words or phrases from the conversation.

10. get_analytics(conversation_id)

    >returns the speaker ratio, talk time, silence, pace and overlap from the conversation.

>example for demonstrate the use of conversation class
>
```
import symbl

conversation_id=1234567890 # Update with the conversation Id of your conversation

print(symbl.Conversations.get_messages(conversation_id))
```

>to access more insights click [here](https://github.com/symblai/symbl-python/tree/main/example/Conversation_Class/conversation_class.py)

# Telephony class

Based on PSTN and SIP protocols, the Telephony API provides an interface for the developers to have Symbl bridge/join VoIP calls and get the results back in real-time as well. Optionally, the developer can also trigger an email at the end of the conversation containing the URL to view the transcription, insights and topics in a single page Web Application.


1. start_pstn(phoneNumber, dtmf, actions, data):
    >Parameter Name | Required | Value
    >--- | --- | ---
    >phoneNumber | Mandatory | phoneNumber where symbl should call
    >dtmf | Optional | dtmf sequence to entered by symbl to join the call
    >credentials | optional | Don't add this parameter if you have `symbl.conf` file in your home directory or working directory
    >actions | Optional | follows the following pattern `[{invokeOn: "stop", name: "sendSummaryEmail", parameters: {emails: ["email@example.com"]}}]`
    >data | optional | `{session: {name: "sessionName"}}`
    >languages | optional | To provide the Language list explicitly
    >timezone | optional | To provide timezone explicitly
    
    >returns connection object
    >
    >click [here](https://github.com/symblai/symbl-python/tree/main/example/Telephony_API/telephony_pstn.py) to check the example for usage of parameters/arguments and connection object
    >
    >For more details check [here][telephony-docs]

2. start_sip(uri, audioConfig, actions, data):
    
    >Parameter Name | Required | Value
    >--- | --- | ---
    >uri | Mandatory | uri where symbl should connect
    >audioConfig | Optional | audioConfigs of the SIP 
    >credentials | optional | Don't add this parameter if you have `symbl.conf` file in your home directory or working directory
    >actions | Optional | follows the following pattern `[{invokeOn: "stop", name: "sendSummaryEmail", parameters: {emails: ["email@example.com"]}}]`
    >data | optional | `{session: {name: "sessionName"}}`
    >languages | optional | To provide the Language list explicitly
    >timezone | optional | To provide timezone explicitly
    
    >returns connection object
    >
    >click [here]https://github.com/symblai/symbl-python/tree/main/example/Telephony_API/telephony_sip.py) to check the example for usage of parameters/arguments and connection object
    >
    >For more details check [here][telephony-docs]

3. stop(connectionId):

    >Parameter Name | Required | Value
    >--- | --- | ---
    >connection_id | Mandatory | connection id of the conversation is required to stop the connection
    
    >only `connection_id` parameter is required
    >
    >returns an updated connection object which will have the conversationId in the response.
    
    >You can subscribe the following events for Telephony API by the connection object
    > 1. **insight_response**:- generates an event whenever a question or an action_item is found.
    > 2. **message_response**:- generates an event whenever a transcription is available.
    > 3. **transcript_response**:- (Part of telephony API only), these are also transcription values, however these will include an isFinal property which will be False initially meaning the transcription are not finalized.
    > 4. **tracker_response**:- It will generate an event whenever a tracker is identified in any transcription.
    > 5. **topic_response**:- It will generate an event whenever a topic is identified in any transcription.
    
    >by this way you can subscribe the events
    >
     ```
     import symbl
        events = {transcript_response': lambda transcript: print('printing the transcript response ', str(transcript))}

        sip_uri = "<sip_url>"
        connection_object = symbl.Telephony.start_sip(uri=sip_uri)

        connection_object.subscribe(events)
    ```

# Streaming class

Symbl's Streaming API is based on WebSocket protocol and can be used for real-time use-cases where both the audio and its results from Symbl's back-end need to be available in real-time.

1. start_connection(credentials=None, speaker=None, insight_types=None):
    >Parameter Name | Required | Value
    >--- | --- | ---
    >credentials | optional | Don't add this parameter if you have `symbl.conf` file in your home directory or working directory
    >speaker | Optional | speaker object containing `name` and `email` field
    >insight_type | Optional |  insight_types to be available in the websocket connection.
    >config | optional | using this parameter you can pass confidenceThreshold, languageCode
    >languages | optional | To provide the Language list explicitly
    >timezone | optional | To provide timezone explicitly
    
    >returns connection object
    >
    >click [here](https://github.com/symblai/symbl-python/tree/main/example/Streaming_API/streaming.py) to check the example for usage of parameters/arguments and connection object
    >
    >For more details check [here][streaming-docs]

    >You can subscribe the following events for Streaming API by the connection object
    > 1. **insight_response**:- generates an event whenever a question or an action_item is found.
    > 2. **message_response**:- generates an event whenever a transcription is available.
    > 3. **tracker_response**:- It will generate an event whenever a tracker is identified in any transcription.
    > 4. **topic_response**:- It will generate an event whenever a topic is identified in any transcription.
    > 5. **message**:- (Part of streaming API only), It will generate an event for live transcriptions. It will include isFinal property which will be False initially, meaning the transcription is not finalized.

    >by this way you can subscribe the events
    >
     ```
    events = {
        'message_response': lambda response: print('Final Messages -> ', [message['payload']['content'] for message in response['messages']])}

    insight_types = ['question', 'action_item']

    connection_object = symbl.Streaming.start_connection(
        insight_types=insight_types)

    connection_object.subscribe(events)

    connection_object.send_audio_from_mic()
    ```
    >
## connection object

The connection object is returned by telephony API's start_pstn & start_sip or Streaming API' start_connection function. A connection object can be utilized for communicating with Symbl Server through underlying websocket implementation.

1. connection.subscribe({'event': callback, ...}):
    >
    >**subscribe function can be used with both Telephony as well as Streaming class**
    >
    >takes a dictionary parameter, where the key can be an event and it's value can be a callback function that should be executed on the occurrence of that event.
    >
    >The list of events that can be subscribed by connection object are:-
    >
    > 1. **insight_response** :- generates an event whenever a question or an action_item is found.
    > 2. **message_response**:- generates an event whenever a transcription is available.
    > 3. **transcript_response**:- (Part of telephony API), these are also transcription values, however these will include an isFinal property which will be False initially meaning the transcription are not finalized.
    > 4. **tracker_response**:- It will generate an event whenever a tracker is identified in any transcription.
    > 5. **topic_response**:- It will generate an event whenever a topic is identified in any transcription.
    > 6. **message**:- (Part of stremaing API), It will generate an event for live transcriptions. It will include isFinal property which will be False initially, meaning the transcription is not finalized.
    >
    >you can define the events like this
    >
    >
    ```
    events = {'message_response': lambda message: print('printing the transcription', str(message)),
    'insight_response': lambda insight: print('printing the insight response ', str(insight))}
    ```

2. connection.stop():
    >
    >**stop function can be used with both Telephony as well as Streaming class**
    >
    >used to stop the telephony connection.

3. connection.send_audio_from_mic(device=None):
    >
    >**send_audio_from_mic function can be used with Streaming class only**
    >
    >Uses sounddevice library to take input from User's mic and send data to websocket directly. Recommended function for first time users.
    >
    >device parameter can take the deviceId (integer) as input, for more information see sd.query_devices() [here][sound_device-query_devices]
    >
    >If this function is not running correctly, please make sure the sounddevice library is installed correctly and has access to your microphone. For more details, check [here][sound_device-installation]

4. connection.send_audio(data):
    >
    >**send_audio function can be used with Streaming class only**
    >
    >Can be used when user is willing to send custom audio data from some other library.
    >
    >send_audio function sends audio data to websockets in binary format.

5. Conversation Object :- 
    >Connection object has a conversation parameter, through which you can directly query the conversation api with the provided conversationId.
    >

    ```python

    import symbl

    connection_object = symbl.Streaming.start_connection()

    ...

    connection_object.conversation.get_topics()

    ```

[api-keys]: https://platform.symbl.ai/#/login
[symbl-docs]: https://docs.symbl.ai/docs/
[text_payload-docs]: https://docs.symbl.ai/docs/async-api/overview/text/post-text#code-example-1
[telephony-docs]: https://docs.symbl.ai/docs/telephony-api/api-reference#endpoint
[streaming-docs]: https://docs.symbl.ai/docs/streaming-api/api-reference#request-parameters
[audio_api-class]: https://github.com/symblai/symbl-python/blob/main/symbl/readme.md#audio-class
[video_api-class]: https://github.com/symblai/symbl-python/blob/main/symbl/readme.md#video-class
[text_api-class]: https://github.com/symblai/symbl-python/blob/main/symbl/readme.md#text-class
[conversation_api-class]: https://github.com/symblai/symbl-python/blob/main/symbl/readme.md#conversations-class
[telephony_api-class]: https://github.com/symblai/symbl-python/blob/main/symbl/readme.md#telephony-class
[streaming_api-class]: https://github.com/symblai/symbl-python/blob/main/symbl/readme.md#streaming-class
[sound_device-query_devices]: https://python-sounddevice.readthedocs.io/en/0.3.12/api.html#sounddevice.query_devices
[sound_device-installation]: https://python-sounddevice.readthedocs.io/en/0.4.1/installation.html
