import symbl
id1 = "abcd"

payload_streaming={
    "speakerEvents" : [
    {
        "type": "started_speaking",
        "user": {
            "id": id1,
            "name": "john",
                "email": "john@example.com"
        },
        "offset": {
            "seconds": 52,
            "nanos": 5000000000
        }
    },
    {
        "type": "stopped_speaking",
        "user": {
            "id": id1,
            "name": "john",
            "email": "john@example.com"
        },
        "offset": {
            "seconds": 15,
            "nanos": 5000000000
        }
    }
    ]
}
Conversation_id = "1234567890" # update with valid conversation id
print(symbl.Conversations.put_speakers_events(Conversation_id, payload_streaming))

print(symbl.Conversations.get_members(Conversation_id))
