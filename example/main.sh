#!/bin/sh
. /env.sh
echo "$(date)" >> /var/log/cron.log 2>&1
/opt/conda/bin/python /main.py >> /var/log/cron.log 2>&1
