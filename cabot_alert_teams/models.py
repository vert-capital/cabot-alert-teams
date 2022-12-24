from cabot.cabotapp.alert import AlertPlugin, AlertPluginUserData
from django.template import Context, Template

from cabot_alert_teams.msbot import send_message

email_template = """Service <b>{{ service.name }}</b><br>
<a target='_blank' href='{{ scheme }}://{{ host }}{% url 'service' pk=service.id %}'>{{ scheme }}://{{ host }}{% url 'service' pk=service.id %}</a><br> {% if service.overall_status != service.PASSING_STATUS %}alerting
with status: {{ service.overall_status }}{% else %}is back to normal{% endif %}.<br>
{% if service.overall_status != service.PASSING_STATUS %}
CHECKS FAILING:{% for check in service.all_failing_checks %}
  FAILING - {{ check.name }} - Type: {{ check.check_category }} - Importance:
   <b>{{ check.get_importance_display }}</b>{% endfor %}
{% if service.all_passing_checks %}
Passing checks:{% for check in service.all_passing_checks %}
  PASSING - {{ check.name }} - Type: {{ check.check_category }} - Importance:
  <b>{{ check.get_importance_display }}</b>{% endfor %}
{% endif %}
{% endif %}
"""


class TeamsAlert(AlertPlugin):
    name = "Teams"
    author = "Thiago Freitas"

    def send_alert(self, service, users, duty_officers):
        emails = set([u.email for u in users if u.email])

        c = Context(
            {
                "service": service,
                "host": "cabot.vert-capital.app",
                "scheme": "https",
            }
        )

        if service.overall_status != service.PASSING_STATUS:
            if service.overall_status == service.CRITICAL_STATUS:
                emails.update([u.email for u in duty_officers if u.email])
            subject = "<b>%s</b> status for service: <b>%s</b>" % (
                service.overall_status,
                service.name,
            )
        else:
            subject = "Service back to normal: <b>%s</b>" % (service.name,)
        if not emails:
            return

        print("************************************")
        print("************************************")
        print("ALETA POR TEAMS")
        print("teste 1111")

        t = Templaate(email_template)
        message = "<b>APP OFFLINE STATUS</b><br>" + subject + "<br>" + t.render(c)

        emails = list(emails)

        print("teste 22222")
        send_message(
            emails,
            message,
        )


class TeamsAlertUserData(AlertPluginUserData):
    name = "Teams"
