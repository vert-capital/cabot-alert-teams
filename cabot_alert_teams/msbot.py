import json
import os

import requests


def send_message(to, message, content_type="html", importance="normal"):
    """
    Send message to Microsoft Teams
    """

    payload = json.dumps(
        {
            "users": to,
            "message": message,
            "importance": importance,
            "contentType": content_type,
        }
    )

    url = os.environ.get("MSBOT_URL", "") + "api/send-message-users"

    headers = {
        "Authorization": os.environ.get("MSBOT_KEY", ""),
        "Content-Type": "application/json",
    }

    requests.request("POST", url, headers=headers, data=payload)
