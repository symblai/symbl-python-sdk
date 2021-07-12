from symbl.utils.Threads import Thread
import symbl
import time

# here are all events supported by Telephony API, you just need to uncomment the event which you would like to use
events = {
    'transcript_response': lambda transcript: print('printing the transcript response ', str(transcript))
    ,'message_response': lambda message: print('printing the message response ', str(message))
    #,'insight_response': lambda insight: print('printing the insight response ', str(insight))
    #,'tracker_response': lambda tracker: print('printing the tracker response ', str(tracker))
    #,'topic_response': lambda topic: print('printing the topic response ', str(topic))
}

sip_uri = "<sip_url>"
connection_object = symbl.Telephony.start_sip(uri=sip_uri)

connection_object.subscribe(events)

# you can get the response from the conversation object, when you will stop the connection explicitly using keyboard interrupt or by using
# connection_object.stop() 

# To get the message from the conversation
#print(connection_object.conversation.get_messages())

# To get the action items from the conversation
# print(connection_object.conversation.get_action_items())

# To get the follow ups from the conversation
# print(connection_object.conversation.get_follow_ups())

# To get the members information from the conversation
# print(connection_object.conversation.get_members())

# To get the topics from the conversation
# print(connection_object.conversation.get_topics())

# To get the questions from the conversation
# print(connection_object.conversation.get_questions())
