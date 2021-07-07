# Symbl Python SDK

The Symbl Python SDK provides convenient access to the Symbl API from applications written in the Python language. It includes a pre-defined set of classes for a simple and clear utilization of APIs.

## Documentation

See the [Python API docs](https://docs.symbl.ai/docs/).

### Requirements

- Python 2.7+ or Python 3.4+ (PyPy supported)

## Installation

First make sure that Python is installed in your system.

To install the python, just visit the links mentioned below:

Windows: https://phoenixnap.com/kb/how-to-install-python-3-windows
Mac: https://flaviocopes.com/python-installation-macos/

You don't need this source code unless you want to modify the package. If you just
want to use the package, then you can install it, either using 'pip' or with 'source':

>just run the command mentioned below to install using 'pip':

```sh
pip install --upgrade symbl
```

>or you can also install the package with source:

```sh
python setup.py install
```

## Configuration

The library needs to be configured with your account's credentials (appId & appSecret) which is
available in your [Symbl Platform][api-keys].

You can either provide the credentials by saving a file named symbl.conf in your working directory or home directory in the following format.

>Home directory will be C:/Users/\<Your Username\> on your windows system, or ~ in your Linux or Mac system.

```conf
[credentials]
app_id=<app_id>
app_secret=<app_secret>
```
Example for 'symbl.conf' file

```conf
[credentials]
app_id=1234567890 #Update with your app_id, without any quotes
app_secret=abcdefghijklmnop #Update with your app_secret, without any quotes
```
## A speech to text converter under 5 lines of code

To know more about **Async Audio Api**, click [here][async_audio-docs]. To know more about the Python SDK Audio Package, click [here][extended_readme-audio]

```python
import symbl

# Process audio file
conversation_object = symbl.Audio.process_file(
  # credentials={app_id: <app_id>, app_secret: <app_secret>}, #Optional, Don't add this parameter if you have symbl.conf file in your home directory
  file_path=<file_path>)

# Printing transcription messages
print(conversation_object.get_messages())
```

To know more about conversation object and it's functions, click [here][extended_readme-conversation-object]

## Extracting insights from Textual conversation

To know more about **Async Text Api**, click [here][async_text-docs]. To know more about the Python SDK Text Package, click [here][extended_readme-text]

  ``` python

import symbl

payload = {
  "messages": [
    {
      "payload": {"content": "Hi Anthony. I saw your complaints about bad call reception on your mobile phone. Can I know what issues you are currently facing?"},
      "from": {"userId": "surbhi@example.com","name": "Surbhi Rathore"}
    },
    {
      "payload": {"content": "Hey Surbhi, thanks for reaching out. Whenever I am picking up the call there is a lot of white noise and I literally can’t hear anything."},
      "from": {"userId": "anthony@example.com","name": "Anthony Claudia"}
    },
    {
      "payload": {"content": "Okay. I can schedule a visit from one of our technicians for tomorrow afternoon at 1:00 PM. He can look at your mobile and handle any issue right away"},
      "from": {"userId": "surbhi@example.com","name": "Surbhi Rathore"}
    },
    {
      "payload": {"content": "That will be really helpful. I'll follow up with the technician about some other issues too, tomorrow"},
      "from": {"userId": "anthony@example.com","name": "Anthony Claudia"}
    },
    {
      "payload": {"content": "Sure. We are happy to help. I am scheduling the visit for tomorrow. Thanks for using Abccorp networks. Have a good day."},
      "from": {"userId": "surbhi@example.com","name": "Surbhi Rathore"}
    }
  ]
}

conversation_object = symbl.Text.process(payload=payload)

print(conversation_object.get_messages())
print(conversation_object.get_topics())
print(conversation_object.get_action_items())
print(conversation_object.get_follow_ups())

  ```

## Analysis of your Zoom Call on your email (Symbl will join your zoom call and send you analysis on provided email)

To know more about **telephony api**, click [here][telephony_api-docs]. To know more about the Python SDK Telephony Package, click [here][extended_readme-telephony]

```python

import symbl

phoneNumber = "" # Zoom phone number to be called, check here https://us02web.zoom.us/zoomconference
meetingId = "" # Your zoom meetingId
password = "" # Your zoom meeting passcode
emailId = ""

connection_object = symbl.Telephony.start_pstn(
      # credentials={app_id: <app_id>, app_secret: <app_secret>}, #Optional, Don't add this parameter if you have symbl.conf file in your home directory or working directory
      phone_number=phoneNumber,
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
    )

print(connection_object)

```

## Live audio transcript using your system's microphone

To know more about **streaming api**, click [here][streaming_api-docs]. To know more about the Python SDK Streaming Package, click [here][extended_readme-streaming]

```python
import symbl

connection_object = symbl.Streaming.start_connection()

connection_object.subscribe({'message_response': lambda response: print('got this response from callback', response)})

connection_object.send_audio_from_mic()
```

## Extended Readme

You can see all the functions provided by SDK in the **extended [readme.md][extended-readme] file**.

You can go through some examples for understanding the use of all functionality [Explore more example](https://github.com/symblai/symbl-python/tree/main/example)

## Possible Errros

1. PortAudio Errors on Mac Systems:-

   If you're getting PortAudio Error which looks like this
    > sounddevice.PortAudioError: Error opening InputStream: Internal PortAudio error [PaErrorCode -9986]
  
   Please consider updating the PortAudio library in your system. Running the following command can help.
    > brew install portaudio

## Need support

If you are looking for some specific use cases do check our [examples][examples] folder.

If you can't find your answers, do let us know at support@symbl.ai or join our slack channel [here][slack-invite].

[api-keys]: https://platform.symbl.ai/#/login
[symbl-docs]: https://docs.symbl.ai/docs/
[streaming_api-docs]: https://docs.symbl.ai/docs/streamingapi/introduction
[telephony_api-docs]: https://docs.symbl.ai/docs/telephony/introduction
[async_text-docs]: https://docs.symbl.ai/docs/async-api/overview/text/post-text/
[async_audio-docs]: https://docs.symbl.ai/docs/async-api/overview/audio/post-audio
[extended-readme]: https://github.com/symblai/symbl-python/blob/main/symbl/readme.md
[extended_readme-conversation-object]: https://github.com/symblai/symbl-python/blob/main/symbl/readme.md#conversation-object
[extended_readme-streaming]: https://github.com/symblai/symbl-python/blob/main/symbl/readme.md#streaming-class
[extended_readme-telephony]: https://github.com/symblai/symbl-python/blob/main/symbl/readme.md#telephony-class
[extended_readme-text]: <https://github.com/symblai/symbl-python/blob/main/symbl/readme.md#text-class>
[extended_readme-audio]: https://github.com/symblai/symbl-python/blob/main/symbl/readme.md#audio-class
[examples]: https://github.com/symblai/symbl-python/tree/main/example
[unicodeerror]: https://stackoverflow.com/questions/37400974/unicode-error-unicodeescape-codec-cant-decode-bytes-in-position-2-3-trunca
[slack-invite]: https://symbldotai.slack.com/join/shared_invite/zt-4sic2s11-D3x496pll8UHSJ89cm78CA#/
