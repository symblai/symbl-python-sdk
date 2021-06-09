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

if __name__ == '__main__':
    unittest.main()
