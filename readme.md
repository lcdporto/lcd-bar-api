# lcd-bar API

Created with the cookiecutter-api-starter

## Documentation

(add documentation link)

## Planning

(add planning link)

## Cronjobs

(add cronjobs like this)

```
# every minute, send queued emails
* * * * * /usr/bin/docker exec lcdbar-api python3 manage.py send_queued_mail > /home/solo/logs/lcdbar/api_cron.log 2>&1

```