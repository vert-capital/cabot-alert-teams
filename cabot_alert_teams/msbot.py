import json
import os

import requests


def send_message(to, message):
    """
    Send message to Microsoft Teams
    """

    payload = json.dumps(
        {
            "users": to,
            "message": message,
            "importance": "high",
            "contentType": "html",
        }
    )

    url = os.environ.get("MSBOT_URL", "") + "api/send-message-users"

    headers = {
        "Authorization": os.environ.get("MSBOT_KEY", ""),
        "Content-Type": "application/json",
    }

    print("Sending message to MS Teams")
    print(url)
    print(payload)
    print("token:", os.environ.get("MSBOT_KEY", ""))

    requests.request("POST", url, headers=headers, data=payload)
