from symbl.Conversations import Conversation

import unittest
from unittest.mock import Mock, patch

from types import SimpleNamespace


class ConversationsTest(unittest.TestCase):

    def test_get_messages_should_succeed_given_valid_conversation_id(self):
        demo_response = SimpleNamespace(**{"messages":[{"id":"6125275260649472","text":"Hey, is this a question?","from":{},"startTime":"2021-05-27T13:19:25.270Z","endTime":"2021-05-27T13:19:26.770Z","conversationId":"6549352073920512","phrases":[]}]})
        conversations_object = Conversation("6549352073920512")

        with patch("symbl.AuthenticationToken.get_api_client", Mock(return_value="None")), patch("symbl.ConversationsApi.get_messages", Mock(return_value=demo_response)):
            self.assertEqual(demo_response, conversations_object.get_messages())

    def test_get_action_items_should_succeed_given_valid_conversation_id(self):
        demo_response = SimpleNamespace(**{"actionItems":[{"id":"4755377456414720","text":"Steve needs to complete the analysis by next Monday.","type":"action_item","score":0.9765610554943914,"messageIds":["5590459222065152"],"entities":[{"type":"daterange","text":"by next monday","offset":39,"end":"2021-06-07"},{"type":"person","text":"Steve","offset":0,"value":{"assignee":True,"id":"98d11b11-4a0a-4bdd-b2e1-d50238f605d6","name":"Steve","userId":"Steve@example.com"}}],"phrases":[],"from":{"id":"98d11b11-4a0a-4bdd-b2e1-d50238f605d6","name":"Steve","userId":"Steve@example.com"},"definitive":True,"assignee":{"id":"98d11b11-4a0a-4bdd-b2e1-d50238f605d6","name":"Steve","email":"Steve@example.com"}}]})
        conversations_object = Conversation("6549352073920512")

        with patch("symbl.AuthenticationToken.get_api_client", Mock(return_value="None")), patch("symbl.ConversationsApi.get_action_items", Mock(return_value=demo_response)):
            self.assertEqual(demo_response, conversations_object.get_action_items())

    def test_get_follow_ups_should_succeed_given_valid_conversation_id(self):
        demo_response = SimpleNamespace(**{"followUps":[{"id":"4529863081852928","text":"Steve needs to follow up about this next Monday.","type":"follow_up","score":1,"messageIds":["5399026486738944"],"entities":[{"type":"date","text":"next monday","offset":38,"value":"2021-06-07"},{"type":"person","text":"Steve","offset":0,"value":{"assignee":True,"id":"e2219a6c-ec5e-4412-94d7-46f565ba5eb7","name":"Steve","userId":"Steve@example.com"}}],"phrases":[],"from":{"id":"e2219a6c-ec5e-4412-94d7-46f565ba5eb7","name":"Steve","userId":"Steve@example.com"},"definitive":True,"assignee":{"id":"e2219a6c-ec5e-4412-94d7-46f565ba5eb7","name":"Steve","email":"Steve@example.com"}}]})
        conversations_object = Conversation("6549352073920512")

        with patch("symbl.AuthenticationToken.get_api_client", Mock(return_value="None")), patch("symbl.ConversationsApi.get_follow_ups", Mock(return_value=demo_response)):
            self.assertEqual(demo_response, conversations_object.get_follow_ups())

    def test_get_members_should_succeed_given_valid_conversation_id(self):
        demo_response = SimpleNamespace(**{"members":[{"id":"25f497bd-2800-4e2b-bc71-e143a8f71d6b","name":"Steve","email":"steve@abccorp.com"}]})
        conversations_object = Conversation("6549352073920512")

        with patch("symbl.AuthenticationToken.get_api_client", Mock(return_value="None")), patch("symbl.ConversationsApi.get_members", Mock(return_value=demo_response)):
            self.assertEqual(demo_response, conversations_object.get_members())

    def test_get_questions_should_succeed_given_valid_conversation_id(self):
        demo_response = SimpleNamespace(**{"questions":[{"id":"4784246146203648","text":"Will you be reviewint the analysis by next Monday?","type":"question","score":0.9833490590134427,"messageIds":["4580678118146048"],"from":{"id":"ca0fcd23-dc63-4d42-894a-43ca84650f6f","name":"Steve","userId":"Steve@example.com"}}]})
        conversations_object = Conversation("6549352073920512")

        with patch("symbl.AuthenticationToken.get_api_client", Mock(return_value="None")), patch("symbl.ConversationsApi.get_questions", Mock(return_value=demo_response)):
            self.assertEqual(demo_response, conversations_object.get_questions())

    def test_get_topics_should_succeed_given_valid_conversation_id(self):
        demo_response = SimpleNamespace(**{"topics":[{"id":"5506508885327872","text":"video","type":"topic","score":0.064,"messageIds":["5823121492803584","4673825691140096"],"parentRefs":[]}]})
        conversations_object = Conversation("6549352073920512")

        with patch("symbl.AuthenticationToken.get_api_client", Mock(return_value="None")), patch("symbl.ConversationsApi.get_topics", Mock(return_value=demo_response)):
            self.assertEqual(demo_response, conversations_object.get_topics())

    def test_get_conversation_should_succeed_given_valid_conversation_id(self):
        demo_response = SimpleNamespace(**{"id": "5102778889273344","type": "meeting","name": "TestingTextAPI","startTime": "2021-07-27T07:11:04.304Z","endTime": "2021-07-27T07:13:19.184Z","members": [{"id": "461dd687-4341-48a5-9f3a-7f6019d6378c","name": "John","email": "john@example.com"}]})
        conversations_object = Conversation("6549352073920512")

        with patch("symbl.AuthenticationToken.get_api_client", Mock(return_value="None")), patch("symbl.ConversationsApi.get_conversation", Mock(return_value=demo_response)):
            self.assertEqual(demo_response, conversations_object.get_conversation())


    def test_get_analytics_should_succeed_given_valid_conversation_id(self):
        demo_response = SimpleNamespace(**{"metrics": [{"type": "total_silence","percent": 0,"seconds": 0},{"type": "total_talk_time","percent": 100,"seconds": 134.88},{"type": "total_overlap","percent": 0,"seconds": 0}],"members": [{"id": "461dd687-4341-48a5-9f3a-7f6019d6378c","name": "John","userId": "john@example.com","pace": {"wpm": 124},"talkTime": {"percentage": 100,"seconds": 134.88},"listenTime": {"percentage": 0,"seconds": 0},"overlap": {}}]})
        conversations_object = Conversation("6549352073920512")

        with patch("symbl.AuthenticationToken.get_api_client", Mock(return_value="None")), patch("symbl.ConversationsApi.get_analytics", Mock(return_value=demo_response)):
            self.assertEqual(demo_response, conversations_object.get_analytics())

    def test_get_trackers_should_succeed_given_valid_conversation_id(self):
        demo_response = SimpleNamespace(**{ "id": "5243525907087360", "name": "text_tracker", "matches": [ { "messageRefs": [ { "id": "5867975128121344", "text": "I don't know which platform is it, but I came to know that platform.", "offset": 19 }, { "id": "6328818106105856", "text": "So this is a live demo that we are trying to give very we are going to show how the platform detects various insights can do transcription in real time and also the different topics of discussions, which would be generated after the call is over, and they will be an email that will be sent to the inbox.", "offset": 84 } ], "type": "vocabulary", "value": "platform", "insightRefs": [] } ] })
        conversations_object = Conversation("6549352073920512")

        with patch("symbl.AuthenticationToken.get_api_client", Mock(return_value="None")), patch("symbl.ConversationsApi.get_trackers", Mock(return_value=demo_response)):
            self.assertEqual(demo_response, conversations_object.get_trackers())

    def test_get_entities_should_succeed_given_valid_conversation_id(self):
        demo_response = SimpleNamespace(**{"entities":[{"custom_type":"None","type":"person","value":"richard holmes","text":"richard holmes","end":"None","start":"None","messageRefs":[{"id":"5895830172073984","text":"We need to have the meeting today, and we're going to talk about how to run a product strategy Workshop is by Richard Holmes.","offset":111}]}]})
        conversations_object = Conversation("6549352073920512")

        with patch("symbl.AuthenticationToken.get_api_client", Mock(return_value="None")), patch("symbl.ConversationsApi.get_entities", Mock(return_value=demo_response)):
            self.assertEqual(demo_response, conversations_object.get_entities())

    def test_get_analytics_should_succeed_given_valid_conversation_id(self):
        demo_response = SimpleNamespace(**{"metrics": [{"type": "total_silence","percent": 0,"seconds": 0},{"type": "total_talk_time","percent": 100,"seconds": 134.88},{"type": "total_overlap","percent": 0,"seconds": 0}],"members": [{"id": "461dd687-4341-48a5-9f3a-7f6019d6378c","name": "John","userId": "john@example.com","pace": {"wpm": 124},"talkTime": {"percentage": 100,"seconds": 134.88},"listenTime": {"percentage": 0,"seconds": 0},"overlap": {}}]})
        conversations_object = Conversation("6549352073920512")

        with patch("symbl.AuthenticationToken.get_api_client", Mock(return_value="None")), patch("symbl.ConversationsApi.get_analytics", Mock(return_value=demo_response)):
            self.assertEqual(demo_response, conversations_object.get_analytics())

    
if __name__ == '__main__':
    unittest.main()
