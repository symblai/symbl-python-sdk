from symbl.conversations_api.ConversationsApi import ConversationsApi

import unittest
from unittest.mock import Mock, patch

from types import SimpleNamespace


class ConversationsApiTest(unittest.TestCase):

    def test_get_messages_should_succeed_given_valid_conversation_id(self):
        demo_response = SimpleNamespace(**{"messages": [{"id": "6125275260649472", "text": "Hey, is this a question?", "from": {
        }, "startTime": "2021-05-27T13:19:25.270Z", "endTime": "2021-05-27T13:19:26.770Z", "conversationId": "6549352073920512", "phrases": []}]})
        conversations_api = ConversationsApi()

        with patch("symbl.AuthenticationToken.get_api_client", Mock(return_value="None")), patch("symbl_rest.ConversationsApi.get_messages_by_conversation_id", Mock(return_value=demo_response)):
            self.assertEqual(
                demo_response, conversations_api.get_messages("6549352073920512"))

    def test_get_action_items_should_succeed_given_valid_conversation_id(self):
        demo_response = SimpleNamespace(**{"actionItems": [{"id": "4755377456414720", "text": "Steve needs to complete the analysis by next Monday.", "type": "action_item", "score": 0.9765610554943914, "messageIds": ["5590459222065152"], "entities":[{"type": "daterange", "text": "by next monday", "offset": 39, "end": "2021-06-07"}, {"type": "person", "text": "Steve", "offset": 0, "value": {
                                        "assignee": True, "id": "98d11b11-4a0a-4bdd-b2e1-d50238f605d6", "name": "Steve", "userId": "Steve@example.com"}}], "phrases": [], "from":{"id": "98d11b11-4a0a-4bdd-b2e1-d50238f605d6", "name": "Steve", "userId": "Steve@example.com"}, "definitive": True, "assignee": {"id": "98d11b11-4a0a-4bdd-b2e1-d50238f605d6", "name": "Steve", "email": "Steve@example.com"}}]})
        conversations_api = ConversationsApi()

        with patch("symbl.AuthenticationToken.get_api_client", Mock(return_value="None")), patch("symbl_rest.ConversationsApi.get_action_items_by_conversation_id", Mock(return_value=demo_response)):
            self.assertEqual(
                demo_response, conversations_api.get_action_items("6549352073920512"))

    def test_get_follow_ups_should_succeed_given_valid_conversation_id(self):
        demo_response = SimpleNamespace(**{"followUps": [{"id": "4529863081852928", "text": "Steve needs to follow up about this next Monday.", "type": "follow_up", "score": 1, "messageIds": ["5399026486738944"], "entities":[{"type": "date", "text": "next monday", "offset": 38, "value": "2021-06-07"}, {"type": "person", "text": "Steve", "offset": 0, "value": {
                                        "assignee": True, "id": "e2219a6c-ec5e-4412-94d7-46f565ba5eb7", "name": "Steve", "userId": "Steve@example.com"}}], "phrases": [], "from":{"id": "e2219a6c-ec5e-4412-94d7-46f565ba5eb7", "name": "Steve", "userId": "Steve@example.com"}, "definitive": True, "assignee": {"id": "e2219a6c-ec5e-4412-94d7-46f565ba5eb7", "name": "Steve", "email": "Steve@example.com"}}]})
        conversations_api = ConversationsApi()

        with patch("symbl.AuthenticationToken.get_api_client", Mock(return_value="None")), patch("symbl_rest.ConversationsApi.get_follow_ups_by_conversation_id", Mock(return_value=demo_response)):
            self.assertEqual(
                demo_response, conversations_api.get_follow_ups("6549352073920512"))

    def test_get_members_should_succeed_given_valid_conversation_id(self):
        demo_response = SimpleNamespace(
            **{"members": [{"id": "25f497bd-2800-4e2b-bc71-e143a8f71d6b", "name": "Steve", "email": "steve@abccorp.com"}]})
        conversations_api = ConversationsApi()

        with patch("symbl.AuthenticationToken.get_api_client", Mock(return_value="None")), patch("symbl_rest.ConversationsApi.get_members_by_conversation_id", Mock(return_value=demo_response)):
            self.assertEqual(
                demo_response, conversations_api.get_members("6549352073920512"))

    def test_get_questions_should_succeed_given_valid_conversation_id(self):
        demo_response = SimpleNamespace(**{"questions": [{"id": "4784246146203648", "text": "Will you be reviewint the analysis by next Monday?", "type": "question", "score": 0.9833490590134427, "messageIds": [
                                        "4580678118146048"], "from":{"id": "ca0fcd23-dc63-4d42-894a-43ca84650f6f", "name": "Steve", "userId": "Steve@example.com"}}]})
        conversations_api = ConversationsApi()

        with patch("symbl.AuthenticationToken.get_api_client", Mock(return_value="None")), patch("symbl_rest.ConversationsApi.get_questions_by_conversation_id", Mock(return_value=demo_response)):
            self.assertEqual(
                demo_response, conversations_api.get_questions("6549352073920512"))

    def test_get_topics_should_succeed_given_valid_conversation_id(self):
        demo_response = SimpleNamespace(**{"topics": [{"id": "5506508885327872", "text": "video", "type": "topic",
                                        "score": 0.064, "messageIds": ["5823121492803584", "4673825691140096"], "parentRefs":[]}]})
        conversations_api = ConversationsApi()

        with patch("symbl.AuthenticationToken.get_api_client", Mock(return_value="None")), patch("symbl_rest.ConversationsApi.get_topics_by_conversation_id", Mock(return_value=demo_response)):
            self.assertEqual(
                demo_response, conversations_api.get_topics("6549352073920512"))

    def test_get_conversation_should_succeed_given_valid_conversation_id(self):
        demo_response = SimpleNamespace(**{"id": "5102778889273344", "type": "meeting", "name": "TestingTextAPI", "startTime": "2021-07-27T07:11:04.304Z",
                                        "endTime": "2021-07-27T07:13:19.184Z", "members": [{"id": "461dd687-4341-48a5-9f3a-7f6019d6378c", "name": "John", "email": "john@example.com"}]})
        conversations_api = ConversationsApi()

        with patch("symbl.AuthenticationToken.get_api_client", Mock(return_value="None")), patch("symbl_rest.ConversationsApi.get_conversation_by_conversation_id", Mock(return_value=demo_response)):
            self.assertEqual(
                demo_response, conversations_api.get_conversation("6549352073920512"))

    def test_get_trackers_should_succeed_given_valid_conversation_id(self):
        demo_response = SimpleNamespace(**{"id": "5243525907087360", "name": "text_tracker", "matches": [{"messageRefs": [{"id": "5867975128121344", "text": "I don't know which platform is it, but I came to know that platform.", "offset": 19}, {
                                        "id": "6328818106105856", "text": "So this is a live demo that we are trying to give very we are going to show how the platform detects various insights can do transcription in real time and also the different topics of discussions, which would be generated after the call is over, and they will be an email that will be sent to the inbox.", "offset": 84}], "type": "vocabulary", "value": "platform", "insightRefs": []}]})
        conversations_api = ConversationsApi()

        with patch("symbl.AuthenticationToken.get_api_client", Mock(return_value="None")), patch("symbl_rest.ConversationsApi.get_trackers_by_conversation_id", Mock(return_value=demo_response)):
            self.assertEqual(
                demo_response, conversations_api.get_trackers("6549352073920512"))

    def test_get_entities_should_succeed_given_valid_conversation_id(self):
        demo_response = SimpleNamespace(**{"entities": [{"custom_type": "None", "type": "person", "value": "richard holmes", "text": "richard holmes", "end": "None", "start": "None", "messageRefs": [
                                        {"id": "5895830172073984", "text": "We need to have the meeting today, and we're going to talk about how to run a product strategy Workshop is by Richard Holmes.", "offset": 111}]}]})
        conversations_api = ConversationsApi()

        with patch("symbl.AuthenticationToken.get_api_client", Mock(return_value="None")), patch("symbl_rest.ConversationsApi.get_entities_by_conversation_id", Mock(return_value=demo_response)), patch("symbl.utils.Helper.parse_entity_response", Mock(return_value=demo_response)):
            self.assertEqual(
                demo_response, conversations_api.get_entities("6549352073920512"))

    def test_get_analytics_should_succeed_given_valid_conversation_id(self):
        demo_response = SimpleNamespace(**{"metrics": [{"type": "total_silence", "percent": 0, "seconds": 0}, {"type": "total_talk_time", "percent": 100, "seconds": 134.88}, {"type": "total_overlap", "percent": 0, "seconds": 0}], "members": [
                                        {"id": "461dd687-4341-48a5-9f3a-7f6019d6378c", "name": "John", "userId": "john@example.com", "pace": {"wpm": 124}, "talkTime": {"percentage": 100, "seconds": 134.88}, "listenTime": {"percentage": 0, "seconds": 0}, "overlap": {}}]})
        conversations_api = ConversationsApi()

        with patch("symbl.AuthenticationToken.get_api_client", Mock(return_value="None")), patch("symbl_rest.ConversationsApi.get_analytics_by_conversation_id", Mock(return_value=demo_response)):
            self.assertEqual(
                demo_response, conversations_api.get_analytics("6549352073920512"))

    def test_put_members_should_succeed_given_valid_conversation_id(self):
        demo_response = SimpleNamespace(
            **{"message": "Member with id: 1234567890 for conversationId: 6549352073920512 updated successfully! The update should be reflected in all messages and insights along with this conversation"})
        conversations_api = ConversationsApi()

        param = {"id": "1234567890",
                 "email": "john@example.in",
                 "name": "john"}

        with patch("symbl.AuthenticationToken.get_api_client", Mock(return_value="None")), patch("symbl_rest.ConversationsApi.put_members_information_by_members_id", Mock(return_value=demo_response)):
            self.assertEqual(demo_response, conversations_api.put_members(
                "6549352073920512","1234567890", param))

    def test_put_speakers_events_should_succeed_given_valid_conversation_id(self):
        demo_response = SimpleNamespace(
            **{"message": "Speaker events associated for conversationId: 6549352073920512 successfully! The update should be reflected in all messages and insights along with this conversation"})
        conversations_api = ConversationsApi()

        payload_streaming = {
            "speakerEvents": [
                {
                    "type": "started_speaking",
                    "user": {
                        "id": "1234567890",
                        "name": "john",
                        "email": "john@example.com"
                    },
                    "offset": {
                        "seconds": 52,
                        "nanos": 5000000000
                    }
                }
            ]
        }

        with patch("symbl.AuthenticationToken.get_api_client", Mock(return_value="None")), patch("symbl_rest.ConversationsApi.put_speakers_event_by_conversation_id", Mock(return_value=demo_response)):
            self.assertEqual(demo_response, conversations_api.put_speakers_events(
                "6549352073920512", payload_streaming))


if __name__ == '__main__':
    unittest.main()
