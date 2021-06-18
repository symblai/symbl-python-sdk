import symbl

file = "D:\Hani\Symbl\Internship\Material\sample_video_file (1).mp4"
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
conversation = symbl.Video.process_file(file_path=file, parameters=params)

print("Members : ",conversation.get_members())
print("Conversation data : ", conversation.get_conversation_data())
print("Messages : ",conversation.get_messages())

'''
import symbl

file = "D:\Hani\Symbl\Internship\Material\sample_video_file (1).mp4"

conversation_id = "4640348266561536" #update with your conversation ID

conversation = symbl.Video.append_file(file_path=file, conversation_id=conversation_id)

print("Members : ",conversation.get_members())
print("Conversation data : ", conversation.get_conversation_data())
print("Messages : ",conversation.get_messages())
'''