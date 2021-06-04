
from symbl.telephony_api.TelephonyApi import TelephonyApi
import unittest
from unittest.mock import Mock, patch

from types import SimpleNamespace


class TelephonyTest(unittest.TestCase):

    def test_start_pstn_should_succeed_given_valid_phone(self):
        demo_response = SimpleNamespace(**{"event_url":"https://api.symbl.ai/v1/event/7025ecfa-a050-40aa-aa2d-0628b6d097b5","result_web_socket_url":"wss://api.symbl.ai/events/7025ecfa-a050-40aa-aa2d-0628b6d097b5","conversation_id":"5219424513556480","connection_id":"7025ecfa-a050-40aa-aa2d-0628b6d097b5"})
        demo_actions = [{"invokeOn": "stop", "name": "sendSummaryEmail", "parameters": { "emails": [ "example@example.com"  ]}}]
        telephony_class = TelephonyApi()

        with patch("symbl.AuthenticationToken.get_api_client", Mock(return_value="None")), patch("symbl_rest.ConnectionToEndpointApi.connect_to_endpoint", Mock(return_value=demo_response)):
            self.assertEqual(demo_response.conversation_id, telephony_class.start_pstn('demophone', actions=demo_actions).conversation.get_conversation_id())

    def test_start_sip_should_succeed_given_valid_sip(self):
        demo_response = SimpleNamespace(**{"event_url":"https://api.symbl.ai/v1/event/7025ecfa-a050-40aa-aa2d-0628b6d097b5","result_web_socket_url":"wss://api.symbl.ai/events/7025ecfa-a050-40aa-aa2d-0628b6d097b5","conversation_id":"5219424513556480","connection_id":"7025ecfa-a050-40aa-aa2d-0628b6d097b5"})
        telephony_class = TelephonyApi()

        with patch("symbl.AuthenticationToken.get_api_client", Mock(return_value="None")), patch("symbl_rest.ConnectionToEndpointApi.connect_to_endpoint", Mock(return_value=demo_response)):
            self.assertEqual(demo_response.conversation_id, telephony_class.start_sip('demophone').conversation.get_conversation_id())

    # def test_start_sip_should_succeed_given_valid_sip(self):
    #     demo_response = SimpleNamespace(**{"event_url":"https://api.symbl.ai/v1/event/7025ecfa-a050-40aa-aa2d-0628b6d097b5","result_web_socket_url":"wss://api.symbl.ai/events/7025ecfa-a050-40aa-aa2d-0628b6d097b5","conversation_id":"5219424513556480","connection_id":"7025ecfa-a050-40aa-aa2d-0628b6d097b5"})
    #     telephony_class = TelephonyApi()

    #     with patch("symbl.AuthenticationToken.get_api_client", Mock(return_value="None")), patch("symbl_rest.ConnectionToEndpointApi.connect_to_endpoint", Mock(return_value=demo_response)):
    #         self.assertEqual(demo_response.connection_id, telephony_class.stop('demophone'))

if __name__ == '__main__':
    unittest.main()
