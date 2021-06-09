from unittest import mock

from symbl.async_api.Audio import Audio, correct_boolean_values
import unittest
from unittest.mock import Mock, patch

from types import SimpleNamespace


class AudioTest(unittest.TestCase):

    def test_correct_boolean_values(self):
        test_dict = {'a': True, 'b': 'true', 'c': 'hello'}
        expected_dict = {'a': 'true', 'b': 'true', 'c': 'hello'}
        self.assertDictEqual(correct_boolean_values(test_dict), expected_dict)

    def test_process_file_should_fail_if_no_file_path(self):
        audio_class = Audio()
        with patch("symbl.AuthenticationToken.get_api_client", Mock(return_value="None")):
            self.assertRaises(TypeError, audio_class.process_file)
            self.assertRaises(ValueError, audio_class.process_file, None)

    def test_process_file_should_succeed_given_valid_path(self):
        demo_response = SimpleNamespace(
            **{"job_id": "demo job id", "conversation_id": "conversationId"})
        demo_job_response = SimpleNamespace(
            **{"job_id": "demo job id", "status": "completed"})
        mock_open = mock.mock_open(read_data=bytes([1, 2, 3, 4, 5, 6, 7, 8]))
        audio_class = Audio()

        with patch('builtins.open', mock_open), patch("symbl.AuthenticationToken.get_api_client",
                                                      Mock(return_value="None")), patch("symbl_rest.AsyncApi.add_audio",
                                                                                        Mock(return_value=demo_response)), patch(
                "symbl_rest.JobsApi.get_job_status", Mock(return_value=demo_job_response)), patch(
                "time.sleep", Mock(return_value=None)
        ):
            self.assertEqual(demo_response.conversation_id, audio_class.process_file(
                'abcd').get_conversation_id())

    def test_process_url_should_succeed_given_valid_url(self):
        demo_response = SimpleNamespace(
            **{"job_id": "demo job id", "conversation_id": "conversationId"})
        demo_job_response = SimpleNamespace(
            **{"job_id": "demo job id", "status": "completed"})
        audio_class = Audio()

        with patch("symbl.AuthenticationToken.get_api_client", Mock(return_value="None")), patch(
                "symbl_rest.AsyncApi.add_audio_url", Mock(return_value=demo_response)), patch(
                "symbl_rest.JobsApi.get_job_status", Mock(return_value=demo_job_response)), patch(
                "time.sleep", Mock(return_value=None)
        ):
            self.assertEqual(demo_response.conversation_id, audio_class.process_url(
                {'url':'abcd'}).get_conversation_id())

    def test_append_file_should_succeed_given_valid_path(self):
        demo_response = SimpleNamespace(
            **{"job_id": "demo job id", "conversation_id": "conversationId"})
        demo_job_response = SimpleNamespace(
            **{"job_id": "demo job id", "status": "completed"})
        mock_open = mock.mock_open(read_data=bytes([1, 2, 3, 4, 5, 6, 7, 8]))
        audio_class = Audio()

        with patch('builtins.open', mock_open), patch("symbl.AuthenticationToken.get_api_client",
                                                      Mock(return_value="None")), patch(
                "symbl_rest.AsyncApi.append_audio", Mock(return_value=demo_response)), patch(
                "symbl_rest.JobsApi.get_job_status", Mock(return_value=demo_job_response)), patch(
                "time.sleep", Mock(return_value=None)
        ):
            self.assertEqual(demo_response.conversation_id,
                             audio_class.append_file('abcd', 'conversationId').get_conversation_id())

    def test_append_url_should_succeed_given_valid_url(self):
        demo_response = SimpleNamespace(
            **{"job_id": "demo job id", "conversation_id": "conversationId"})
        demo_job_response = SimpleNamespace(
            **{"job_id": "demo job id", "status": "completed"})
        audio_class = Audio()

        with patch("symbl.AuthenticationToken.get_api_client", Mock(return_value="None")), patch(
                "symbl_rest.AsyncApi.append_audio_url", Mock(return_value=demo_response)), patch(
                "symbl_rest.JobsApi.get_job_status", Mock(return_value=demo_job_response)), patch(
                "time.sleep", Mock(return_value=None)
        ):
            self.assertEqual(demo_response.conversation_id,
                             audio_class.append_url({'url':'abcd'}, 'conversationId').get_conversation_id())


if __name__ == '__main__':
    unittest.main()
