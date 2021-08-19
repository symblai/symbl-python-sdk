from symbl.utils.Helper import correct_boolean_values, dictionary_to_valid_json, initialize_api_client, insert_valid_boolean_values
from symbl_rest import ConversationsApi as conversations_api_rest
from symbl.utils import Helper

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

    @initialize_api_client      
    def get_conversation(self, conversation_id, credentials=None):
        return self.conversations_api_rest.get_conversation_by_conversation_id(conversation_id)

    @initialize_api_client      
    def get_trackers(self, conversation_id, credentials=None):
        return self.conversations_api_rest.get_trackers_by_conversation_id(conversation_id)

    @initialize_api_client      
    def get_entities(self, conversation_id, credentials=None):
        api_response = self.conversations_api_rest.get_entities_by_conversation_id(conversation_id)
        return Helper.parse_entity_response(api_response) if len(api_response.entities)!=0 else api_response

    @initialize_api_client      
    def get_analytics(self, conversation_id, credentials=None):
        return self.conversations_api_rest.get_analytics_by_conversation_id(conversation_id)

    @initialize_api_client
    def put_members(self, conversation_id, members_id, parameters={}, credentials=None):
        return self.conversations_api_rest.put_members_information_by_members_id(conversation_id, members_id, body=parameters)

    @initialize_api_client
    def put_speakers_events(self, conversation_id, parameters={}, credentials=None):
        return self.conversations_api_rest.put_speakers_event_by_conversation_id(conversation_id, body=parameters)

    @initialize_api_client      
    def delete_conversation(self, conversation_id, credentials=None):
        return self.conversations_api_rest.delete_conversation_by_conversation_id(conversation_id)

    @initialize_api_client      
    def get_formatted_transcript(self, conversation_id, parameters = {},credentials=None):
        content_type = "application/json"
        params = insert_valid_boolean_values(parameters)
        return self.conversations_api_rest.get_formatted_transcript_by_conversation_id(params,content_type,conversation_id)
