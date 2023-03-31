from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/flaskdb'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
