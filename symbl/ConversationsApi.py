from symbl_rest import ConversationsApi as conversations_api_rest

class ConversationsApi():

    def __init__(self, api_client=None):
        '''
            It will initialize the ConversationsApi class
        '''

        if api_client is None:
            raise ValueError('Please initialize sdk with correct app_id and app_secret.')
        
        self.api_client = api_client
        self.conversations_api_rest = conversations_api_rest(api_client)

    def get_action_items(self, conversation_id):
        return self.conversations_api_rest.get_action_items_by_conversation_id(conversation_id)

    def get_follow_ups(self, conversation_id ):  
        return self.conversations_api_rest.get_follow_ups_by_conversation_id(conversation_id)

    def get_insights(self, conversation_id):  
        return self.conversations_api_rest.get_insights_by_conversation_id(conversation_id)
        
    def get_members(self, conversation_id):  
        return self.conversations_api_rest.get_members_by_conversation_id(conversation_id)
        
    def get_messages(self, conversation_id):  
        return self.conversations_api_rest.get_messages_by_conversation_id(conversation_id)
        
    def get_questions(self, conversation_id):  
        return self.conversations_api_rest.get_questions_by_conversation_id(conversation_id)
        
    def get_topics(self, conversation_id):  
        return self.conversations_api_rest.get_topics_by_conversation_id(conversation_id)
