import symbl


# here you can add more events which support the Streaming API like 'insight_response', 'message_response' etc.
events = {
    'message': lambda message: print('printing the message response ', str(message))
   # ,'message_response': lambda message: print('printing the transcription', str(message))
   # ,'insight_response': lambda insight: print('printing the insight response ', str(insight))
    #,'tracker_response': lambda tracker: print('printing the tracker response ', str(tracker))
   # ,'topic_response': lambda topic: print('printing the topic response ', str(topic))
}


#To access the Trackers API, you will need to specify 'tracker_response' event
trackers = [{
    "name": "tracker_name",
    "vocabulary": [
        "hello",
        "vocabulary_2",
        "vocabulary_n"
    ]
}]


insight_types = ['question', 'action_item']

speaker = {
    'userId': 'John@example.com',
    'name': 'John',
}

connection_object = symbl.Streaming.start_connection(
    insight_types=insight_types, speaker=speaker,trackers=trackers)

connection_object.subscribe(events)

connection_object.send_audio_from_mic()

# you can get the response from the conversation object, when you will stop the connection explicitly 
# or Python SDK will detect the silence in the on going conversation

#To get the message from the conversation
#print(connection_object.conversation.get_messages())

#To get the conversation data from the conversation
#print(connection_object.conversation.get_conversation())

#To get the action items from the conversation
#print(connection_object.conversation.get_action_items())

#To get the follow ups from the conversation
#print(connection_object.conversation.get_follow_ups())

#To get the members information from the conversation
#print(connection_object.conversation.get_members())

#To get the topics from the conversation
#print(connection_object.conversation.get_topics())

#To get the questions from the conversation
#print(connection_object.conversation.get_questions())

# To get the analytics from the conversation
#print(connection_object.conversation.get_analytics())

