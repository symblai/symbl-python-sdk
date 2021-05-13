from __future__ import absolute_import
from symbl_rest import  JobsApi, ApiClient

from symbl.async_api.Audio import Audio
from symbl.async_api.Video import Video
from symbl.async_api.Text import Text

from symbl.conversations_api.ConversationsApi import ConversationsApi
from symbl.telephony_api.TelephonyApi import TelephonyApi
from symbl.jobs_api.Job import Job
from symbl.jobs_api.JobStatus import JobStatus

Audio = Audio()
Video = Video()
Text = Text()
Conversations = ConversationsApi()
telephony_api = TelephonyApi()