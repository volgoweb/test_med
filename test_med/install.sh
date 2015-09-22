#! /bin/bash
sudo apt-get install python-virtualenv
virtualenv --no-site-packages --distribute -p /usr/bin/python3.4 venv
source venv/bin/activate
pip install -r test_med/app/requirements.txt
python test_med/manage.py syncdb --noinput
python test_med/manage.py migrate
python test_med/manage.py loaddata demo_accounts.json
