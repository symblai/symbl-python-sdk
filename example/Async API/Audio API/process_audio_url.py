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

payload = {
    'url': "<url>" #write the url path of the audio, which you want to process
    }
conversation = symbl.Audio.process_url(payload=payload)

print(conversation.get_conversation())
print(conversation.get_messages())
#print(conversation.get_action_items())
#print(conversation.get_follow_ups())
#print(conversation.get_members())
#print(conversation.get_topics())
#print(conversation.get_questions())

