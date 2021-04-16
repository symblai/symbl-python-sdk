from __future__ import absolute_import
from symbl.TelephonyApi import TelephonyApi

from symbl_rest import AuthenticationApi, JobsApi, ApiClient, Configuration
from symbl.AsyncApi import AsyncApi

from symbl.AsyncApi import AsyncApi
from symbl.ConversationsApi import ConversationsApi
from symbl.Job import Job
from symbl.JobStatus import JobStatus

api_client = None
async_api = None
conversations_api = None
telephony_api = None


'''
    It will return an object of ApiClient with a prefilled token. 
'''

def init(app_id=None, app_secret=None, refresh_token=False):

    if app_id is None or len(app_id) == 0:
        raise ValueError('app_id is required')
    
    if app_secret is None or len(app_secret) == 0:
        raise ValueError('app_secret is required')

    configuration = Configuration()

    body={
        'type': 'application', 
        'appId': app_id, 
        'appSecret': app_secret
        }

    authenticationResponse = AuthenticationApi().generate_token(body)
    configuration.api_key['x-api-key'] = authenticationResponse.access_token

    global api_client, async_api, conversations_api, telephony_api
    api_client = ApiClient(configuration)
    async_api = AsyncApi(api_client)
    conversations_api = ConversationsApi(api_client)
    telephony_api = TelephonyApi(api_client)