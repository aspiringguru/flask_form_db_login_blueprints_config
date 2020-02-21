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

add .gitignore and setup git repo, exclude the environment directory  

create simplest possible version of flask app

python simplest_app.py
http://localhost:5000/

now migrate to the config methodology

add
start.sh
nb: use vim editor to avoid <CR> dos2unix syntax related errors.

simplest demo > start.sh configure with > FLASK_APP=simplest_app.py

https://github.com/aspiringguru/flask_form_db_login_blueprints_config/tree/470d460e781562467c245b5d4a3b80b9654616cb

then upgrade to use application


pip install Flask-Assets
pip3 install flask-assets lesscpy cssmin jsmin

tree -I 'env|.git|__pycache__'
-------------------------------------------------
.
├── README.md
├── application
│   ├── __init__.py
│   ├── assets.py
│   ├── routes.py
│   ├── static
│   └── templates
│       └── simplest_template.html
├── config.py
├── simplest_app.py
├── start.sh
└── wsgi.py
-------------------------------------------------
https://github.com/aspiringguru/flask_form_db_login_blueprints_config/tree/0ea5369bb6c18c3ab5334ede70b1b9638de04f51


------------------------------------------------
pip freeze

Click==7.0
cssmin==0.2.0
Flask==1.1.1
Flask-Assets==2.0
itsdangerous==1.1.0
Jinja2==2.11.1
jsmin==2.2.2
lesscpy==0.14.0
MarkupSafe==1.1.1
pkg-resources==0.0.0
ply==3.11
six==1.14.0
webassets==2.0
Werkzeug==1.0.0
------------------------------------------------

added application/static/dist/ files. several .css, .js.
added application/static/src/ files.
less files are similar format to .css files.
https://hackersandslackers.com/static-assets-flask/
https://flask-assets.readthedocs.io/en/latest/

start.sh > FLASK_APP=wsgi.py
wsgi.py > ~/application/__init__.py > def create_app

add SQLAlchemy & LoginManager features to __init__.py
