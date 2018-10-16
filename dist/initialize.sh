#!/bin/bash

# copy and enable nginx virtual host configuration
cp ./dist/api /etc/nginx/sites-available/
ln -s /etc/nginx/sites-available/api /etc/nginx/sites-enabled/api

# in development mode
if [ "$APP_IN_PRODUCTION" != "true" ]; then
    # migrations are automatic
    python3 /var/www/manage.py migrate --noinput
    # static files are collected on container init
    python3 /var/www/manage.py collectstatic --noinput

    # NOTE: if plugs-mail installed uncomment next line
    # python3 /var/www/manage.py load_email_templates
fi

# NOTE: if plugs-media installed uncomment next line
cp -R --remove-destination /var/www/lcdbar/api/static/api/default/ /var/www/lcdbar/api/static/media/

python3 /var/www/manage.py createcachetable

exit 0