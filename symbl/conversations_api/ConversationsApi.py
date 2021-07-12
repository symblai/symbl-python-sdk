from symbl.utils.Helper import correct_boolean_values, dictionary_to_valid_json, initialize_api_client
from symbl_rest import ConversationsApi as conversations_api_rest


class ConversationsApi():

    def __init__(self):
        '''
            It will initialize the ConversationsApi class
        '''
        
        self.conversations_api_rest = conversations_api_rest()

    @initialize_api_client
    def get_action_items(self, conversation_id, credentials=None):
        return self.conversations_api_rest.get_action_items_by_conversation_id(conversation_id)

    @initialize_api_client
    def get_follow_ups(self, conversation_id, credentials=None ):  
        return self.conversations_api_rest.get_follow_ups_by_conversation_id(conversation_id)

    @initialize_api_client      
    def get_members(self, conversation_id, credentials=None):  
        return self.conversations_api_rest.get_members_by_conversation_id(conversation_id)
  
    @initialize_api_client      
    def get_messages(self, conversation_id, credentials=None, parameters={}):  
        params = dictionary_to_valid_json(parameters)
        return self.conversations_api_rest.get_messages_by_conversation_id(conversation_id, **correct_boolean_values(params))
  
    @initialize_api_client      
    def get_questions(self, conversation_id, credentials=None):  
        return self.conversations_api_rest.get_questions_by_conversation_id(conversation_id)
  
    @initialize_api_client      
    def get_topics(self, conversation_id, credentials=None, parameters={}):
        params = dictionary_to_valid_json(parameters)
        return self.conversations_api_rest.get_topics_by_conversation_id(conversation_id, **correct_boolean_values(params))
