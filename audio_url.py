import symbl

payload = {
    'url': "https://symbltestdata.s3.us-east-2.amazonaws.com/sample_audio_file.wav",
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


conversation = symbl.Audio.process_url(payload=payload)

print(conversation.get_members())
print(conversation.get_conversation_data())

'''
import symbl

payload = {'url': "https://symbltestdata.s3.us-east-2.amazonaws.com/sample_audio_file.wav"}

conversationId = "6465298258460672"  #update with your conversation Id
conversation = symbl.Audio.append_url(payload=payload, conversation_id=conversationId)

print(conversation.get_members())
print(conversation.get_conversation_data())
print(conversation.get_messages())
'''