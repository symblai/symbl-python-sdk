import symbl

file = "<file_path>"

conversation_id = "1234567890" #update with the conversation ID with which you want to perform the append operation

conversation = symbl.Audio.append_file(file_path=file, conversation_id=conversation_id)

print(conversation.get_messages())
#print(conversation.get_action_items())
#print(conversation.get_follow_ups())
#print(conversation.get_members())
#print(conversation.get_topics())
#print(conversation.get_questions())
