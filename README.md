Cabot Teams Plugin
=====

This is an alert plugin for the cabot service monitoring tool. It allows you to alert users by their user handle in a teams.

## Installation
Enter the cabot virtual environment.
    $ pip install git+https://github.com/vert-capital/cabot-alert-teams.git
    $ foreman stop
Add cabot_alert_teams to the installed apps in settings.py
    $ foreman run python manage.py syncdb
    $ foreman start