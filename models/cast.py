from config import db


class Cast(db.Model):
    
    __tablename__ = 'casts'

    id = db.Column(db.Integer, primary_key=True)
    cast_name = db.Column(db.String(100), nullable=False)
    cast_gender = db.Column(db.String(20), nullable=False)
    cast_character = db.Column(db.String(100), nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'), nullable=False)
    dialogues = db.relationship('Dialogue', backref='cast', lazy=True)