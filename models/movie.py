from config import db


class Movie(db.Model):
    
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    movie_name = db.Column(db.String(100), nullable=False)
    movie_duration = db.Column(db.String(20), nullable=False)
    casts = db.relationship('Cast', backref='movie', lazy=True)
    
    
