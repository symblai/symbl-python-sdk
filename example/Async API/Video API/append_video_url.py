import symbl

payload = {'url': "<url>"} #write the url path of the video, which you want to process

conversationId = "1234567890"  #update with the conversation ID with which you want to perform the append operation
conversation = symbl.Video.append_url(payload=payload, conversation_id=conversationId)

print(conversation.get_messages())
#print(conversation.get_action_items())
#print(conversation.get_follow_ups())
#print(conversation.get_members())
#print(conversation.get_topics())
#print(conversation.get_questions())
