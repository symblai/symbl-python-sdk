import symbl

file = "<file_path>"
''' like this you can pass the parameter
params = {
    'name': "Meeting",
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
conversation = symbl.Audio.process_file(file_path=file, parameters=params)
'''
conversation = symbl.Audio.process_file(file_path=file)

print(conversation.get_conversation())
print(conversation.get_messages())
#print(conversation.get_action_items())
#print(conversation.get_follow_ups())
#print(conversation.get_members())
#print(conversation.get_topics())
#print(conversation.get_questions())
