import symbl

# Audio File containing the Speech Data
conversation = symbl.Audio.process_file(file_path="<file_path>")

# Get Transcription as a JSON Array
transcription_messages = conversation.messages()