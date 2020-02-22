import warnings
from datetime import timedelta

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)

app = Flask(__name__)

app.secret_key = 'sessionData'

app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=5)

app.config['TESTING'] = True

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

app.config['SQLALCHEMY_ECHO'] = True

app.config['SQLALCHEMY_RECORD_QUERIES'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://beec75059e5e00:3bffdb7a@us-cdbr-iron-east-04.cleardb.net:3306/heroku_448e7b8c679cbd1'

app.config['SQLALCHEMY_MAX_OVERFLOW'] = 0

db = SQLAlchemy(app)

print("in project")

import project.com.controller

# conda activate project_conda
# pip install library_name
# conda deactivate project_conda
