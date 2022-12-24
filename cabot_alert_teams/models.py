from cabot.cabotapp.alert import AlertPlugin, AlertPluginUserData
from django.template import Context, Template

from cabot_alert_teams.msbot import send_message

email_template = """Service {{ service.name }} {{ scheme }}://{{ host }}
{% url 'service' pk=service.id %} {% if service.overall_status != service.PASSING_STATUS %}alerting
with status: {{ service.overall_status }}{% else %}is back to normal{% endif %}.
{% if service.overall_status != service.PASSING_STATUS %}
CHECKS FAILING:{% for check in service.all_failing_checks %}
  FAILING - {{ check.name }} - Type: {{ check.check_category }} - Importance:
   {{ check.get_importance_display }}{% endfor %}
{% if service.all_passing_checks %}
Passing checks:{% for check in service.all_passing_checks %}
  PASSING - {{ check.name }} - Type: {{ check.check_category }} - Importance:
  {{ check.get_importance_display }}{% endfor %}
{% endif %}
{% endif %}
"""


class TeamsAlert(AlertPlugin):
    name = "Teams"
    author = "Thiago Freitas"

    def send_alert(self, service, users, duty_officers):
        print("000000")

        emails = set([u.email for u in users if u.email])

        c = Context(
            {
                "service": service,
                "host": "cabot.vert-capital.app",
                "scheme": "https",
            }
        )

        print("service.overall_status", service.overall_status)

        if service.overall_status != service.PASSING_STATUS:
            print("aqui 1")
            if service.overall_status == service.CRITICAL_STATUS:
                emails.update([u.email for u in duty_officers if u.email])
            subject = "%s status for service: %s" % (
                service.overall_status,
                service.name,
            )
        else:
            print("aqui 2")
            subject = "Service back to normal: %s" % (service.name,)
        if not emails:
            print("aqui 3")
            return

        t = Template(email_template)
        message = subject + "<br>" + t.render(c)

        print("emails", emails)
        print("message", message)

        emails = list(emails)

        send_message(
            emails,
            message,
        )


class TeamsAlertUserData(AlertPluginUserData):
    name = "Teams"
