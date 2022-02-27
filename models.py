from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()


class TrendsTitle(db.Model):
    __tablename__ = 'trends_title'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    hashed = db.Column(db.String(200), nullable=True, unique=True)
    stored_date = db.Column(db.DateTime, default=datetime.datetime.now())
    updated_date = db.Column(db.DateTime, nullable=True)
    counters = db.Column(db.Integer)
    link = db.Column(db.String(300), nullable=True)

    def __repr__(self):
        return '<trends title="%s">' % self.title
    @property
    def serialize(self):
        return {
            'title': self.title,
            'hashed': self.hashed,
            'stored_date': self.stored_date,
            'counters': self.counters,
            'link': self.link
        }


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    role = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    updated_at = db.Column(db.DateTime, nullable=True)
    activated = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<User %r>' % self.username
