 

from ctypes import addressof
from datetime import datetime
from types import CoroutineType

from flask import Flask, session, redirect, url_for
from flask import render_template
from flask import request
from flask import Blueprint
from flask import flash
from flask_sqlalchemy import SQLAlchemy


from .models import Checkout, Order_Item, Order, Menus
from . import db
from .forms import  CheckoutForm


customer = Blueprint('customer', __name__)

#-----------------------------------------------------------------------------------
@customer.route('/customer_dashboard', methods=["GET", "POST"])

def dashboard():
   
    return render_template("customer/index.html")

#----------------------------------------------------------------------------------
@customer.route('/breakfast', methods=["GET", "POST"])

def breakfast():
   
    return render_template("customer/breakfast.html")

#----------------------------------------------------------------------------------
@customer.route('/sharings', methods=["GET", "POST"])

def sharings():
   
    return render_template("customer/sharings.html")

#----------------------------------------------------------------------------------
@customer.route('/chicken_deals', methods=["GET", "POST"])

def chickens():
   
    return render_template("customer/chicken_deals.html")


#----------------------------------------------------------------------------------

    

#--------------------------------------------------------------------------------
@customer.route('/checkout', methods=["GET","POST"])

def checkout():
    Checkout_form = CheckoutForm()

    

    if Checkout_form.is_submitted():
        if Checkout_form.validate_on_submit():
            first_name = Checkout_form.first_name.data
            last_name = Checkout_form.last_name.data
            address = Checkout_form.address.data
            County = Checkout_form.county.data
            phone_number = Checkout_form.phone_number.data
            pickup_station = Checkout_form.pickup_station.data

            #creating checkout object
            checkouts=Checkout(
                first_name =first_name,
                last_name = last_name,
                address = address,
                county = County,
                phone_number =phone_number,
                pickup_station = pickup_station  
            )

            try:
                db.session.add(checkouts)
                db.session.commit()
            except Exception as e:
                # for resetting non-commited .add()
                db.session.rollback()
                db.session.flush()
                print("Failed ")
                flash('Database Error')
                print(e)
            else:
                # on successful saving
                flash('successfull.')
                
        else:
            flash("form not validated")  
   
    return render_template("customer/checkout.html", checkout = Checkout_form)

#----------------------------------------------------------------------------------------
@customer.route('/order_history', methods=["GET", "POST"])
def history():
    #--------you create an object linking the database table(checkout)
    checkout = Checkout.query.all()

    return render_template("customer/order_history.html", checkout = checkout)
#----------------------------------------------------------------------------
@customer.route('/add_cart', methods=["GET", "POST"])

def add_cart():
   
    if 'cart' not in session:
        session['cart'] = []

    session['cart'].append({'id': id, 'quantity': 1})
    session.modified = True

    return redirect(url_for('customer.add_cart'))





        
@customer.route('/cart')

def handle_cart():
        products = []
        grand_total = 0
        index = 0
        quantity_total = 0

        for item in session['cart']:
            product = Menus.query.filter_by(id=item['id']).first()

            quantity = int(item['quantity'])
            total = quantity * product.price
            grand_total += total

            quantity_total += quantity

            products.append({'id': product.id, 'name': product.name, 'price':  product.price,
                             'quantity': quantity, 'total': total})
            index += 1

        

        return products, grand_total, quantity_total

def cart():
    products, grand_total, quantity_total = handle_cart()

    return render_template('cart.html', products=products, grand_total=grand_total, quantity_total=quantity_total)
 




@customer.route('/remove-from-cart')
def remove_from_cart(index):
    del session['cart'][int(index)]
    session.modified = True
    return redirect(url_for('cart'))







    