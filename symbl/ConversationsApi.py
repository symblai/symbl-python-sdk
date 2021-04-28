from symbl.AuthenticationToken import get_api_client
from symbl_rest import ConversationsApi as conversations_api_rest

class ConversationsApi():

    def __init__(self, api_client=None):
        '''
            It will initialize the ConversationsApi class
        '''
        
        self.api_client = api_client
        self.conversations_api_rest = conversations_api_rest(api_client)

    def initialize_api_client(self, function):
        def wrapper(*args, **kw):
            credentials = None
            
            if 'credentials' in kw:
                credentials = kw['credentials']

            api_client = get_api_client(credentials)
            self.api_client = api_client
            self.async_api_rest = conversations_api_rest(api_client)

            function(*args, **kw)
        
        return wrapper

    def get_action_items(self, conversation_id, credentials=None):
        def inner(function):
            @self.initialize_api_client
            def wrapper():
                try:
                    return function(self.conversations_api_rest.get_action_items_by_conversation_id(conversation_id))
                except Exception as e:
                    return function(e)
            return wrapper()
        return inner

    
    def get_follow_ups(self, conversation_id, credentials=None ):  
        def inner(function):
            @self.initialize_api_client
            def wrapper():
                try:
                    return function(self.conversations_api_rest.get_follow_ups_by_conversation_id(conversation_id))
                except Exception as e:
                    return function(e)
            return wrapper()
        return inner

    
    def get_insights(self, conversation_id, credentials=None):  
        def inner(function):
            @self.initialize_api_client
            def wrapper():
                try:
                    return function(self.conversations_api_rest.get_insights_by_conversation_id(conversation_id))
                except Exception as e:
                    return function(e)

            return wrapper()
        return inner
  
          
    def get_members(self, conversation_id, credentials=None):
        def inner(function):
            @self.initialize_api_client
            def wrapper():
                try:
                    return function(self.conversations_api_rest.get_members_by_conversation_id(conversation_id))
                except Exception as e:
                    return function(e)
            return wrapper()
        return inner
  
          
    def get_messages(self, conversation_id, credentials=None): 
        def inner(function):
            @self.initialize_api_client
            def wrapper():
                try:
                    return function(self.conversations_api_rest.get_messages_by_conversation_id(conversation_id))
                except Exception as e:
                    return function(e)
            return wrapper()
        return inner
  
          
    def get_questions(self, conversation_id, credentials=None):  
        def inner(function):
            @self.initialize_api_client
            def wrapper():
                try:
                    return function(self.conversations_api_rest.get_questions_by_conversation_id(conversation_id))
                except Exception as e:
                    return function(e)
            return wrapper()
        return inner
  
          
    def get_topics(self, conversation_id, credentials=None): 
        def inner(function):
            @self.initialize_api_client
            def wrapper():
                try:
                    return function(self.conversations_api_rest.get_topics_by_conversation_id(conversation_id))
                except Exception as e:
                    return function(e)
            return wrapper()
        return inner
