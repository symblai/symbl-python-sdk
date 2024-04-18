from conversations_api.ConversationsApi import ConversationsApi

conversations = ConversationsApi();

conversation_id=6750867925630976 # Update with the conversation Id of your conversation

print(conversations.get_call_score(conversation_id))
