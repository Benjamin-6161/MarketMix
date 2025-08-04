from app import db
from .user import User
from .vendor import Vendor

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendor.id'))
    customer_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    customer = db.relationship('User', backref=db.backref('reviews', lazy=True))
    rating = db.Column(db.Integer, nullable=False)
    review = db.Column(db.Text)

    def __repr__(self):
        return f"Review('{self.vendor_id}', '{self.rating}')"