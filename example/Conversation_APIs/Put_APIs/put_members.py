import symbl

Conversation_id = "1234567890" # update with valid conversation id
id = "abcd" # write member's id

param = {"id": id,
         "email": "john@example.in",
         "name": "john"}

print(symbl.Conversations.put_members(Conversation_id, id, parameters= param))
print(symbl.Conversations.get_members(Conversation_id))
