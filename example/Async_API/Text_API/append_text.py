import symbl

payload = {
    "name": "TextAPI",  #you can update the name of the conversation

    "messages": [
    {
      "payload": {"content": "Hi Anthony. I saw your complaints about bad call reception on your mobile phone. Can I know what issues you are currently facing?"},
      "from": {"userId": "surbhi@example.com","name": "Surbhi Rathore"}
    },
    {
      "payload": {"content": "Hey Surbhi, thanks for reaching out. Whenever I am picking up the call there is a lot of white noise and I literally can’t hear anything."},
      "from": {"userId": "anthony@example.com","name": "Anthony Claudia"}
    }
  ]
}

conversation_id = "1234567890" #update with the conversation ID with which you want to perform the append operation

conversation_object = symbl.Text.append(payload=payload, conversation_id=conversation_id)

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