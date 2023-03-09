from config import db


class Dialogue(db.Model):
    
    __tablename__ = 'dialogues'

    id = db.Column(db.Integer, primary_key=True)
    dialogue = db.Column(db.Text, nullable=False)
    start_time = db.Column(db.String(20), nullable=False)
    end_time = db.Column(db.String(20), nullable=False)
    cast_id = db.Column(db.Integer, db.ForeignKey('casts.id', ondelete='SET NULL'))