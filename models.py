import enum
from flask import session
from flask_login import UserMixin
from . import db

class AccountType(enum.Enum):
    EMPLOYEE = "1" #--ADMIN
    CUSTOMER = "0"

class Menus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Integer)
    status =  db.Column(db.String(50))
    description = db.Column(db.String(100))
    category = db.Column(db.String)
    
    orders = db.relationship('Order_Item', backref='Menus', lazy=True)
    def _repr_(self):
        return  "<id:{}>".format(self.id)  


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    user_type = db.Column(db.Enum(AccountType))
   
class Checkout(db.Model):
    address = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String)
    county = db.Column(db.String)
    status =  db.Column(db.String(50))
    phone_number = db.Column(db.Integer)
    pickup_station = db.Column(db.String)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    phone_number = db.Column(db.Integer)
    email = db.Column(db.String(50))
    address = db.Column(db.String(100))
    city = db.Column(db.String(100))
    county = db.Column(db.String(20))
    status = db.Column(db.String(10))
    payment_type = db.Column(db.String(10))

    
class Order_Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('menus.id'))
    quantity = db.Column(db.Integer)