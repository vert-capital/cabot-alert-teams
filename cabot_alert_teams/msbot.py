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

    print("PAYLOAD: ", payload)

    url = os.environ.get("MSBOT_URL", "") + "api/send-message-users"

    print("URL: ", url)

    headers = {
        "Authorization": os.environ.get("MSBOT_KEY", ""),
        "Content-Type": "application/json",
    }

    resp = requests.request("POST", url, headers=headers, data=payload)

    print("RESPONSE: ", resp.text)
