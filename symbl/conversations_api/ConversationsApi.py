from symbl.utils.Helper import correct_boolean_values
from symbl import AuthenticationToken
from symbl_rest import ConversationsApi as conversations_api_rest

def initialize_api_client(function):
    def wrapper(*args, **kw):
        credentials = None
        self = args[0]
        
        if 'credentials' in kw:
            credentials = kw['credentials']

        api_client = AuthenticationToken.get_api_client(credentials)
        self.async_api_rest = conversations_api_rest(api_client)

        return function(*args, **kw)
    
    return wrapper

class ConversationsApi():

    def __init__(self, api_client=None):
        '''
            It will initialize the ConversationsApi class
        '''
        
        self.api_client = api_client
        self.conversations_api_rest = conversations_api_rest(api_client)

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
        return self.conversations_api_rest.get_messages_by_conversation_id(conversation_id, **correct_boolean_values(parameters))
  
    @initialize_api_client      
    def get_questions(self, conversation_id, credentials=None):  
        return self.conversations_api_rest.get_questions_by_conversation_id(conversation_id)
  
    @initialize_api_client      
    def get_topics(self, conversation_id, credentials=None, parameters={}):
        return self.conversations_api_rest.get_topics_by_conversation_id(conversation_id, **correct_boolean_values(parameters))
