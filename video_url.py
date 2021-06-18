'''
import symbl

payload = {
    'url': "https://symbltestdata.s3.us-east-2.amazonaws.com/sample_video_file.mp4",
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


conversation = symbl.Video.process_url(payload=payload)


print("Members : ",conversation.get_members())
print("Conversation data : ", conversation.get_conversation_data())
print("Messages : ",conversation.get_messages())


'''
import symbl

payload = {'url': "https://symbltestdata.s3.us-east-2.amazonaws.com/sample_video_file.mp4"}

conversationId = "4921073972805632"  #update with your conversation Id
conversation = symbl.Video.append_url(payload=payload, conversation_id=conversationId)


print("Members : ",conversation.get_members())
print("Conversation data : ", conversation.get_conversation_data())
print("Messages : ",conversation.get_messages())
