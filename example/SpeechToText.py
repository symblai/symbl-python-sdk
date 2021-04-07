import symbl

# Initialize with credentials
symbl.init(app_id="<app_id>", app_secret="<app_secret>")

# Audio File containing the Speech Data
conversation_id = symbl.async_api.process_audio_file(file_path="<file_path>")

# Get Transcription as a JSON Array
transcription_messages = symbl.conversation_api.get_messages(conversation_id)