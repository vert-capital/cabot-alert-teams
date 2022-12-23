import json

from cabot_alert_teams.kafka import producer


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

    producer("teams-message", payload)
