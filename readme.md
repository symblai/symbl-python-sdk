# Symbl Python SDK

The Symbl Python SDK provides convenient access to the Symbl API from applications written in the Python language. It includes a pre-defined set of classes for a simple and clear utilization of APIs.


## Documentation

See the [Python API docs](https://docs.symbl.ai/docs/).


## Installation

You don't need this source code unless you want to modify the package. If you just
want to use the package, just run:

```sh
pip install --upgrade symbl
```

Install from source with:

```sh
python setup.py install
```

To initialize the SDK, you need to provide app_id and app_token which you can get by signing up on [Symbl Dashboard][api-keys].

You can either provide the api_keys by saving a file named symbl.conf in your home directory in the following format.

```
[credentials]
app_id=<app_id>
app_secret=<app_secret>

```

### Requirements

-   Python 2.7+ or Python 3.4+ (PyPy supported)

### Usages

The library needs to be configured with your account's credentials (appId & appSecret) which is
available in your [Symbl Dashboard][api-keys].


## A speech to text converter under 5 lines of code

```python
import symbl

# Process audio file
conversation = symbl.async_api.process_audio_file(credentials={app_id: <app_id>, app_secret: <app_secret>}, #Optional, Don't add this parameter if you have symbl.conf file in your home directory
file_path=<file_path>)

# Printing transcription messages
print(conversation.messages())
```

## Get topics and action items from your call

```python
import symbl

# Process audio file
conversation = symbl.async_api.process_audio_file(credentials={app_id: <app_id>, app_secret: <app_secret>}, #Optional, Don't add this parameter if you have symbl.conf file in your home directory
file_path=<file_path>)

# Printing topics and actions
print("Topics are = " + str(conversation.topics()))

print("Action Items = " + str(conversation.actions()))
```

## SpeechToText of multiple audio files in a directory 

```python

import symbl
from os import listdir
from os.path import isfile, join

# returns lambda function with fileName which is under processing
def save_transcriptions_in_file(fileName):
    return lambda conversation: on_success(conversation, fileName)

# returns actual callback to save the transcriptions of a conversation in a file
def on_success(conversation, fileName):
    transcriptions = conversation.messages()

    file = open(fileName + ".txt","w+")
    file.write(str(transcriptions))
    file.close()

# Look [here][unicodeerror], if you're getting unicode error
directory_path = r'<directory_path>'

files = [join(directory_path, file) for file in listdir(directory_path) if isfile(join(directory_path, file))]

# Process audio files in the above mentioned directory
for file in files:
    job = symbl.async_api.submit_audio(credentials={app_id: <app_id>, app_secret: <app_secret>}, #Optional, Don't add this parameter if you have symbl.conf file in your home directory
    file_path=file, wait=False).on_complete(save_transcriptions_in_file(file))

```

## Analysis of your Zoom Call on your email (Symbl will join your zoom call and send you analysis on provided email)

```python

import symbl

phoneNumber = "" # Zoom phone number to be called, check here https://us02web.zoom.us/zoomconference
meetingId = "" # Your zoom meetingId
password = "" # Your zoom meeting passcode
emailId = ""

connection = symbl.telephony_api.start_pstn(
      credentials={app_id: <app_id>, app_secret: <app_secret>}, #Optional, Don't add this parameter if you have symbl.conf file in your home directory
      phoneNumber=phoneNumber,
      dtmf = ",,{}#,,{}#".format(meetingId, password),
      actions = [
        {
          "invokeOn": "stop",
          "name": "sendSummaryEmail",
          "parameters": {
            "emails": [
              emailId
            ],
          },
        },
      ]
    })

print(connection)

```

#### Need support

The first place to look for your use case is in the [examples][examples] folder or you can see all the functions provided by SDK in the extended [readme.md][extended-readme] file.

If you can't find your answers, do let us know at support@symbl.ai or join our slack channel [here][slack-invite].

[api-keys]: https://platform.symbl.ai/#/login
[symbl-docs]: https://docs.symbl.ai/docs/
[extended-readme]: https://github.com/symblai/symbl-python/blob/main/symbl/readme.md
[examples]: https://github.com/symblai/symbl-python/tree/main/example
[unicodeerror]: https://stackoverflow.com/questions/37400974/unicode-error-unicodeescape-codec-cant-decode-bytes-in-position-2-3-trunca
[slack-invite]: https://symbldotai.slack.com/join/shared_invite/zt-4sic2s11-D3x496pll8UHSJ89cm78CA#/