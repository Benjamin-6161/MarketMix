from app import db
from .user import User

class Vendor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('vendor', lazy=True))
    business_name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    category = db.Column(db.String(255), nullable=False)
    location = db.Column(db.String(255), nullable=False)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    reviews = db.relationship('Review', backref='vendor', lazy=True)

    def __repr__(self):
        return f"Vendor('{self.business_name}', '{self.category}')"