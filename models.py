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
