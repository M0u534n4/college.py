from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = "gu[xi=71uW_Y3:?uiH}^d1R.l<UQnV.o8^0w}o7V9a4rQ#I!"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"


db = SQLAlchemy(app)