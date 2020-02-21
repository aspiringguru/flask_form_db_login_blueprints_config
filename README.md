### Installing


```
cd /mnt/g/2020_working/coding/flask_form_db_login_blueprints_config

#windows > G:\2020_working\coding\flask_form_db_login_blueprints_config

#my default ubuntu login activates conda. ymmv
conda deactivate
#quick test for default version of python
which python3
python3 --version
#python3 -m venv env
source env/bin/activate
(env)$
which python3
python3 --version
pip install flask
pip freeze


create simplest possible version of flask app

python simplest_app.py
http://localhost:5000/

now migrate to the config methodology

add
start.sh
nb: use vim editor to avoid <CR> dos2unix syntax related errors.

simplest demo > start.sh configure with > FLASK_APP=simplest_app.py

then upgrade to use application
