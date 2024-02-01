#!/bin/bash
# Install DJango app on server

set -e

echo -e "\n>>> Installing Django project files on server"

ssh server /bin/bash << EOF
set -e
echo -e "\n>>>Stop gunicorn"
cd /app/
source env/bin/activate
bash scripts/super.sh stop gunicorn

echo -e "\n>>>Delete old files"
rm -rf /app/ref
rm -rf /app/scripts
rm -rf /app/config
rm requirements.txt

echo -e "\n>>>Copy new files"
cp -r /root/deploy/ref /app/
cp -r /root/deploy/scripts /app/
cp -r /root/deploy/config /app/
cp /root/deploy/requirements.txt /app/

echo -e "\n>>>Install python packages"
pip install -r requirements.txt

echo -e "\n>>>Run Django migrations"
cd ref
./manage.py migrate

echo -e "\n>>>Collect staticfiles"
./manage.py collectstatic
cd ..

echo -e "\n>>>Re-read Supervisord config"
bash scripts/super.sh reread

echo -e "\n>>>Start gunicorn"
bash scripts/super.sh start gunicorn

EOF

echo -e "\n>>> Finished installing Django project files on server"
