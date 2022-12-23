import json

from cabot_alert_teams.kafka import producer


def send_message(
    to: list, message: str, content_type: str = "html", importance: str = "normal"
) -> dict:
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
