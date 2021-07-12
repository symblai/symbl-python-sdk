# SpeechToText of multiple audio files in a directory
# Using this code snippet you can convert multiple audio files from specific directory to the text format 
# It will make seperate .txt files for each audio file into the given directory path and will save the transcriptions of all audio files into those .txt files

import symbl
from os import listdir
from os.path import isfile, join

# returns lambda function with fileName which is under processing
def save_transcriptions_in_file(fileName):
    return lambda conversation_object: on_success(conversation_object, fileName)

# returns actual callback to save the transcriptions of a conversation in a file
def on_success(conversation_object, fileName):
    transcriptions = conversation_object.get_messages()

    file = open(fileName + ".txt","w+")
    file.write(str(transcriptions))
    file.close()

# An ‘r’ preceding a string denotes a raw, (almost) un-escaped string. 
# The escape character is backslash, that is why a normal string will not work as a Windows path string.
# If you are using Mac or Linux, no need to append `r` before <directory path>
directory_path = r'<directory_path>'

files = [join(directory_path, file) for file in listdir(directory_path) if isfile(join(directory_path, file))]

# Process audio files in the above mentioned directory
for file in files:
    job = symbl.Audio.process_file(
      # credentials={app_id: <app_id>, app_secret: <app_secret>}, #Optional, Don't add this parameter if you have symbl.conf file in your home directory
      file_path=file, wait=False).on_complete(save_transcriptions_in_file(file))