from unittest import mock

from symbl.async_api.Text import Text, correct_boolean_values
import unittest
from unittest.mock import Mock, patch

from types import SimpleNamespace


class TextTest(unittest.TestCase):

    def test_correct_boolean_values(self):
        test_dict = {'a': True, 'b': 'true', 'c': 'hello'}
        expected_dict = {'a': 'true', 'b': 'true', 'c': 'hello'}
        self.assertDictEqual(correct_boolean_values(test_dict), expected_dict)

    def test_process_should_fail_if_no_file_path(self):
        text_class = Text()
        with patch("symbl.AuthenticationToken.get_api_client", Mock(return_value="None")):
            self.assertRaises(TypeError, text_class.process)
            self.assertRaises(ValueError, text_class.process, None)

    def test_process_file_should_succeed_given_valid_path(self):
        demo_response = SimpleNamespace(
            **{"job_id": "demo job id", "conversation_id": "conversationId"})
        demo_job_response = SimpleNamespace(
            **{"job_id": "demo job id", "status": "completed"})
        mock_open = mock.mock_open(read_data=bytes([1, 2, 3, 4, 5, 6, 7, 8]))
        text_class = Text()

        with patch('builtins.open', mock_open), patch("symbl.AuthenticationToken.get_api_client",
                                                      Mock(return_value="None")), patch("symbl_rest.AsyncApi.add_text",
                                                                                        Mock(return_value=demo_response)), patch(
                "symbl_rest.JobsApi.get_job_status", Mock(return_value=demo_job_response)), patch("time.sleep",
                                                                                                  Mock(return_value=None)):
            self.assertEqual(demo_response.conversation_id, text_class.process(
                'abcd').get_conversation_id())

    def test_append_should_succeed_given_valid_path(self):
        demo_response = SimpleNamespace(
            **{"job_id": "demo job id", "conversation_id": "conversationId"})
        demo_job_response = SimpleNamespace(
            **{"job_id": "demo job id", "status": "completed"})
        text_class = Text()

        with patch("symbl.AuthenticationToken.get_api_client",
                                                      Mock(return_value="None")), patch(
            "symbl_rest.AsyncApi.append_text", Mock(return_value=demo_response)), patch(
            "symbl_rest.JobsApi.get_job_status", Mock(return_value=demo_job_response)), patch(
            "time.sleep", Mock(return_value=None)
        ):
            self.assertEqual(demo_response.conversation_id,
                             text_class.append('abcd', 'conversationId').get_conversation_id())

if __name__ == '__main__':
    unittest.main()
