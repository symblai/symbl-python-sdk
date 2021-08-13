import symbl

id1 = "abcdefg" #member's Id
id2 = "031c61c" #member's id

payload={
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
    },
    {
            "type": "started_speaking",
            "user": {
                "id":id2,
                "name": "Richard",
                "email": "Richard@example.com"
            },
            "offset": {
                "seconds": 10,
                "nanos": 5000000000
            }
        },
        {
            "type": "stopped_speaking",
            "user": {
                "id": id2,
                "name": "Richard",
                "email": "Richard@example.com"
            },
            "offset": {
                "seconds": 20,
                "nanos": 5000000000
            }
        }
    ]
}

Conversation_id = "1234567890" # update with valid conversation id
print(symbl.Conversations.put_speakers_events(Conversation_id, payload))

print(symbl.Conversations.get_members(Conversation_id))
