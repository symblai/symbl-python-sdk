import symbl

payload = {
    "name": "TextAPI",  #you can update the name of the conversation

    "messages": [
        {
            "duration": {"startTime": "2021-06-18T12:08:19.99Z", "endTime": "2021-06-18T12:10:20.99Z"},

            "payload": {
                "content": "Hello.This is roshani ",
                "contentType": "text/plain"
            },
            "from": {"name": "Roshani", "userId": "roshani@example.com"}
        }
    ]
}

conversation_id = "1234567890" #update with the conversation ID with which you want to perform the append operation

conversation = symbl.Text.append(payload=payload, conversation_id=conversation_id)

print(conversation.get_messages())
#print(conversation.get_action_items())
#print(conversation.get_follow_ups())
#print(conversation.get_members())
#print(conversation.get_topics())
#print(conversation.get_questions())