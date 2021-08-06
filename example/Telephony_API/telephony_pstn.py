
import symbl


phoneNumber = "" # Zoom phone number to be called, which is mentioned into the Zoom meeting invitation
meetingId = "" # Your zoom meetingId
password = "" # Your zoom meeting passcode
emailId = "" # Email address on which you would like to receive the detailed summary of the meeting


# here are all events supported by Telephony API, you just need to uncomment the event which you would like to use
events = {
    'transcript_response': lambda transcript: print('printing the transcript response ', str(transcript))
    ,'message_response': lambda message: print('printing the message response ', str(message))
    #,'insight_response': lambda insight: print('printing the insight response ', str(insight))
    #,'tracker_response': lambda tracker: print('printing the tracker response ', str(tracker))
    #,'topic_response': lambda topic: print('printing the topic response ', str(topic))
}

connection_object = symbl.Telephony.start_pstn(
    phone_number=phoneNumber, 
    dtmf = ",,{}#,,{}#".format(meetingId, password),
    actions = [
        {
          "invokeOn": "stop",
          "name": "sendSummaryEmail",
          "parameters": {
            "emails": [
              emailId
            ],
          },
        },
      ])

connection_object.subscribe(events)

# you can get the response from the conversation object, when you will stop the connection explicitly using keyboard interrupt or by using
# connection_object.stop() # you can also stop the connection after sspecifying some interval of timing

# To get the message from the meeting
#print(connection_object.conversation.get_messages())

#To get the conversation data from the conversation
#print(connection_object.conversation.get_conversation())

# To get the action items from the meeting
# print(connection_object.conversation.get_action_items())

# To get the follow ups from the meeting
# print(connection_object.conversation.get_follow_ups())

# To get the members information from the meeting
# print(connection_object.conversation.get_members())

# To get the topics from the meeting
# print(connection_object.conversation.get_topics())

# To get the questions from the meeting
# print(connection_object.conversation.get_questions())

# To get the analytics from the conversation
#print(connection_object.conversation.get_analytics())

