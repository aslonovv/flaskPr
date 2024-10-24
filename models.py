from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///freelance.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy()
db.init_app(app)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(200), nullable=False)

class Resume(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    experience = db.Column(db.Text, nullable=False)
    skills = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(200), nullable=False)
    city = db.Column(db.String(100), nullable=False)

with app.app_context():
    db.create_all()
