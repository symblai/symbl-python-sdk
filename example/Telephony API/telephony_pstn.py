
import symbl


phoneNumber = "" # Zoom phone number to be called, which is mentioned into the Zoom meeting invitation
meetingId = "" # Your zoom meetingId
password = "" # Your zoom meeting passcode
emailId = "" # Email address on which you would like to receive the detailed summary of the meeting


# here you can add more events which support the Telephony API, for now Telephony API only supports 'transcript_respone'.
events = {
        'transcript_response': lambda response: print('printing the first response ' + str(response)), 
        'insight_response': lambda response: print('printing the first response ' + str(response))
        }


connection = symbl.Telephony.start_pstn(
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

connection.subscribe(events)

# you can get the response from the conversation object, when you will stop the connection explicitly 
# or when Python SDK will detect the silence in the on going conversation

print(connection.conversation.get_conversation())
print(connection.conversation.get_messages())
# print(connection.conversation.get_action_items())
# print(connection.conversation.get_follow_ups())
# print(connection.conversation.get_members())
# print(connection.conversation.get_topics())
# print(connection.conversation.get_questions())

