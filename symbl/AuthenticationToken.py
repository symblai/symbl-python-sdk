from symbl_rest import AuthenticationApi, Configuration, ApiClient

import configparser
import threading
import os

SYMBL_CONFIGURATION_FILENAME = 'symbl.conf'
SYMBL_CREDENTIALS_SECTION = 'credentials'
SYMBL_APP_ID_CONSTANT = 'app_id'
SYMBL_APP_SECRET_CONSTANT = 'app_secret'

configuration = None

cached_app_id = ""
cached_app_secret = ""


config_parser = configparser.ConfigParser()


'''
    It will return an object of ApiClient with a prefilled token. 
'''

def init(app_id=None, app_secret=None):
    if app_id == None and app_secret == None:
        app_id, app_secret = fetchAppCredentialsFromFiles()
    
    generateAndInitializeToken(app_id=app_id, app_secret=app_secret)
    

def generateAndInitializeToken(app_id, app_secret):

    if app_id is None or len(app_id) == 0:
        raise ValueError('app_id is required')
    
    if app_secret is None or len(app_secret) == 0:
        raise ValueError('app_secret is required')
        
    generate_token(app_id, app_secret)

def fetchAppCredentialsFromFiles():
    # configuration file exists in local directory
    if os.path.isfile(SYMBL_CONFIGURATION_FILENAME):
        config_parser.read_file(open(SYMBL_CONFIGURATION_FILENAME))
        if config_parser.has_option(SYMBL_CREDENTIALS_SECTION, SYMBL_APP_ID_CONSTANT) and config_parser.has_option(SYMBL_CREDENTIALS_SECTION, SYMBL_APP_SECRET_CONSTANT):
            return config_parser.get(SYMBL_CREDENTIALS_SECTION, SYMBL_APP_ID_CONSTANT), config_parser.get(SYMBL_CREDENTIALS_SECTION, SYMBL_APP_SECRET_CONSTANT)
        else:
            # configuration file exists in home directory of system
            return fetchAppCredentialsInPath()
    else:
        # configuration file exists in home directory of system
        return fetchAppCredentialsInPath()

def fetchAppCredentialsInPath():
    app_id, app_secret = None, None
    if os.path.isfile("{}/{}".format(os.path.expanduser('~'), SYMBL_CONFIGURATION_FILENAME)):
        config_parser.read_file(open("{}/{}".format(os.path.expanduser('~'), SYMBL_CONFIGURATION_FILENAME)))
        if config_parser.has_option(SYMBL_CREDENTIALS_SECTION, SYMBL_APP_ID_CONSTANT) and config_parser.has_option(SYMBL_CREDENTIALS_SECTION, SYMBL_APP_SECRET_CONSTANT):
            app_id, app_secret =  config_parser.get(SYMBL_CREDENTIALS_SECTION, SYMBL_APP_ID_CONSTANT), config_parser.get(SYMBL_CREDENTIALS_SECTION, SYMBL_APP_SECRET_CONSTANT)

    return app_id, app_secret


def generate_token(app_id, app_secret):
    configuration_instance = Configuration()
    body={
        'type': 'application', 
        'appId': app_id, 
        'appSecret': app_secret
        }

    authenticationResponse = AuthenticationApi().generate_token(body)
    # refreshing token 60 secs before current one expires
    time = authenticationResponse.expires_in

    global configuration
    
    timer = threading.Timer(time, generate_token, args=[app_id, app_secret])
    timer.daemon = True
    timer.start()

    configuration_instance.api_key['x-api-key'] = authenticationResponse.access_token
    configuration = configuration_instance

def get_api_client(credentials=None):

    app_id, app_secret = None, None

    if credentials != None and 'app_id' in credentials:
        app_id = credentials['app_id']
    
    if credentials != None and 'app_secret' in credentials:
        app_secret = credentials['app_secret']

    global configuration
    if configuration == None:
        init(app_id, app_secret)
    return ApiClient(configuration)

def get_api_header(credentials=None):
    app_id, app_secret = None, None

    if credentials != None and 'app_id' in credentials:
        app_id = credentials['app_id']
    
    if credentials != None and 'app_secret' in credentials:
        app_secret = credentials['app_secret']

    global configuration
    if configuration == None:
        init(app_id, app_secret)

    return configuration.api_key

def get_access_token(credentials=None):
    app_id, app_secret = None, None

    if credentials != None and 'app_id' in credentials:
        app_id = credentials['app_id']
    
    if credentials != None and 'app_secret' in credentials:
        app_secret = credentials['app_secret']

    global configuration
    if configuration == None:
        init(app_id, app_secret)

    return configuration.api_key['x-api-key']