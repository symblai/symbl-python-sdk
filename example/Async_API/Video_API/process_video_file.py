import symbl

file = "<file_path>"
''' like this you can pass the parameter
params = {
    'name': "TestingMeeting",
    'enableSpeakerDiarization': "true",
    "diarizationSpeakerCount": "2",
    "channelMetadata": [
            {
                "channel": 1,
                "speaker": {
                    "name": "Robert Bartheon",
                    "email": "robertbartheon@gmail.com"
                }
            },
            {
                "channel": 2,
                "speaker": {
                    "name": "Arya Stark",
                    "email": "aryastark@gmail.com"
                }
            }
        ]
    }
conversation_object = symbl.Video.process_file(file_path=file, parameters=params)
'''
conversation_object = symbl.Video.process_file(file_path=file)


#To get the message from the conversation
print(conversation_object.get_messages())

#To get the conversation data from the conversation
#print(conversation_object.get_conversation())

#To get the action items from the conversation
#print(conversation_object.get_action_items())

#To get the follow ups from the conversation
#print(conversation_object.get_follow_ups())

#To get the members information from the conversation
#print(conversation_object.get_members())

#To get the topics from the conversation
#print(conversation_object.get_topics())

#To get the questions from the conversation
#print(conversation_object.get_questions())

# To get the analytics from the conversation
#print(conversation_object.get_analytics())

# To get the trackers from the conversation
#print(conversation_object.get_trackers())

# To get the entities from the conversation
#print(conversation_object.get_entities())