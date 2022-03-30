import os

from datetime import datetime

from flask import Flask
from flask import render_template
from flask import request
from flask import Blueprint
from flask import flash
from flask_sqlalchemy import SQLAlchemy


from .models import Menus
from . import db
from .forms import add_productForm

admin = Blueprint('admin', __name__)




#-------------------------------------------------------------------------

@admin.route('/', methods=["GET", "POST"])
def home():

    return render_template("index.html")
#------------------------------------------------------------------------

@admin.route('/add_product', methods=["GET", "POST"])
def add_product():
    add_product_form = add_productForm()#--form object

    if add_product_form.is_submitted():
        
        if add_product_form.validate_on_submit():
            product_id = add_product_form.product_id.data
            name = add_product_form.name.data
            category = add_product_form.category.data
            price = add_product_form.category.data
            quantity = add_product_form.quantity.data
            status = add_product_form.status.data
            description = add_product_form.description.data
            file_photo = add_product_form.photo.data

            # create menu product object(database object)
            menu = Menus(
                id = product_id,
                name = name,
                quantity = quantity,
                price = price,
                status =  status,
                description = description,
                category = category,
                photo = file_photo
            )


            
            try:
                db.session.add(menu)
                db.session.commit()
            except Exception as e:
                # for resetting non-commited .add()
                db.session.rollback()
                db.session.flush()
                print("Failed to add product")
                flash('Database Error: Failed to process product')
                print(e)
            else:
                # on successful saving
                flash('Product was added successfully.')
                
        else:
            flash("form not validated")  
            

        
        
        
    return render_template("admin/add_product.html", add_product = add_product_form)#--you pass object and the form label
        
#-----------------------------------------------------------------------------
@admin.route('/view_menu', methods=["GET", "POST"])
def view_menu():
    menus = Menus.query.all()

    return render_template("admin/view_menu.html", menus = menus)

#-----------------------------------------------------------------------------
@admin.route('/product_detail', methods=["GET", "POST"])
def product_detail():
    menus = Menus.query.all()

    return render_template("admin/product_detail.html", menus = menus)

#---------------------------------------------------------------------------
@admin.route('/menu_grid', methods=["GET", "POST"])
def menu_grid():
    

    return render_template("admin/menu_grid.html")
#----------------------------------
