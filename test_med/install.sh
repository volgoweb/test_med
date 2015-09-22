#! /bin/bash
sudo apt-get install python-virtualenv
virtualenv --no-site-packages --distribute -p /usr/bin/python3.4 venv
source venv/bin/activate
pip install -r app/requirements.txt
python manage.py syncdb --noinput
python manage.py migrate
python manage.py loaddata demo_accounts.json
