import symbl

payload = {'url': "<url>"} #write the url path of the video, which you want to process

conversationId = "1234567890"  #update with the conversation ID with which you want to perform the append operation
conversation_object = symbl.Video.append_url(payload=payload, conversation_id=conversationId)


#To get the message from the conversation
print(conversation_object.get_messages())

#To get the conversation data from the conversation
#print(conversation_object.get_conversation())

#To get the action items from the conversation
#print(conversation_object.get_action_items())

#To get the follow ups from the conversation
#print(conversation_object.get_follow_ups())

#To get the members information from the conversation
#print(conversation_object.get_members())

#To get the topics from the conversation
#print(conversation_object.get_topics())

#To get the questions from the conversation
#print(conversation_object.get_questions())

# To get the analytics from the conversation
#print(conversation_object.get_analytics())

# To get the trackers from the conversation
#print(conversation_object.get_trackers())

# To get the entities from the conversation
#print(conversation_object.get_entities())