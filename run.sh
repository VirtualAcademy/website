#!/bin/bash

#echo STARTING RUN.SH FOR DJANGO SERVER PORT
#
#echo ENVIRONMENT VARIABLES IN RUN.SH
#printenv

if [ -z "$VCAP_APP_PORT"];
	then SERVER_PORT=5000;
	else SERVER_PORT="$VCAP_APP_PORT";
fi
echo setting environmental var
export ENV_ROLE='production'
export WEDIN_KEY="tgs)tj=z(-g(h7@#g21a=d_e9+pv2c=)b7bev2srzau5p%-+y#"
echo [$0] port is------------------------- $SERVER_PORT
python manage.py migrate --noinput
echo "from django.contrib.auth.models import User; User.objects.create_superuser('cho', 'cho_ndi@yahoo.com', 'cho123')" | python manage.py shell

echo [$0] Starting Django Server...
python manage.py runserver 0.0.0.0:$SERVER_PORT --noreload