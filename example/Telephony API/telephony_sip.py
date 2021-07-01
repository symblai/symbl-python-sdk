import symbl

# here you can add more events which support the Telephony API, like tracker_response, topic_response etc.
events = {
    'transcript_response': lambda transcript: print('printing the first response ', str(transcript))
}
connection = symbl.Telephony.start_sip(uri="sip:8002@sip.rammer.ai")

connection.subscribe(events)

# you can get the response from the conversation object, when you will stop the connection explicitly 
# or when Python SDK will detect the silence in the on going conversation

print(connection.conversation.get_messages())
# print(connection.conversation.get_action_items())
# print(connection.conversation.get_follow_ups())
# print(connection.conversation.get_members())
# print(connection.conversation.get_topics())
# print(connection.conversation.get_questions())

