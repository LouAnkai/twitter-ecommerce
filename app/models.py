from app import app, db

class Title(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
