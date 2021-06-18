import symbl

file = "D:\Hani\Symbl\Internship\Material\sample_audio_file.wav"
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
conversation = symbl.Audio.process_file(file_path=file, parameters=params)

print(conversation.get_members())
print(conversation.get_conversation_data())
print(conversation.get_messages())


'''
import symbl

file = "D:\Hani\Symbl\Internship\Material\Call Center Sample Calls- E-Commerce Store.mp3"

conversation_id = "6579318768533504" #update with your conversation ID

conversation = symbl.Audio.append_file(file_path=file, conversation_id=conversation_id)

print("Members : ",conversation.get_members())
print("Conversation data : ", conversation.get_conversation_data())
print("Messages : ",conversation.get_messages())
'''
