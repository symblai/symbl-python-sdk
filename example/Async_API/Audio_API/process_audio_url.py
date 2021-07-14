import symbl
'''
you can also pass other parameters with the payload 
payload = {
    'url': "<url>", #write the url path of the audio, which you want to process
    'name': "TestingMeeting",
    'enableSpeakerDiarization': "true",
    'diarizationSpeakerCount': "2",
    'channelMetadata': [
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
'''

payload = {'url': "<url>"} #write the url path of the audio, which you want to process
conversation_object = symbl.Audio.process_url(payload=payload)

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