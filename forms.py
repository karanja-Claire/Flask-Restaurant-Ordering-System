from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SubmitField, SelectField, HiddenField

from wtforms.validators import InputRequired, NumberRange, Length
from flask_wtf.file import FileField, FileRequired, FileAllowed




class add_productForm(FlaskForm):
    # id is autoincrement, no need to set it up manually. You can have a sperate field for product id, which is unique and still have an autoincrement  primary key for your table
    product_id = IntegerField('product id', validators=[InputRequired()])
    name = TextAreaField('name of the product', validators=[InputRequired(),Length(min=4, max=30)])
    category = SelectField('select category', choices=[(1,'Small'),(2,'Medium'),(3,'Large')], validators=[InputRequired()],)
    price = IntegerField('price', validators=[InputRequired(),
        NumberRange(min=1.00, max=999.99)])
    quantity = IntegerField('quantity', validators=[InputRequired(), NumberRange(min=1, max=999)])
    status = SelectField('select status', choices =[(1,'Available'),(2,'Out of stock')], validators=[InputRequired()],)
    description = TextAreaField('Description')
    file_photo = FileField(validators=[FileAllowed('photos', 'Image only!'), FileRequired('File was empty!')])
    save= SubmitField('Save')
    delete = SubmitField('delete')

class CheckoutForm(FlaskForm):
    first_name = TextAreaField('first name', validators=[InputRequired(),Length(min=4, max=30)])
    last_name =TextAreaField('second name', validators=[InputRequired(),Length(min=4, max=30)])
    address = IntegerField('address', validators=[InputRequired()])
    county = SelectField('county', choices=[(1,'Nairobi'),(2,'Kiambu')], validators=[InputRequired()],)
    phone_number = IntegerField('phonenumber', validators=[InputRequired()])
    pickup_station =  SelectField('county', choices=[(1,'Nairobi-CBD'),(2,'Kiambu-Thika')], validators=[InputRequired()],)
    save= SubmitField('Save')

class AddToCart(FlaskForm):
    quantity = IntegerField('Quantity')
    id = HiddenField('ID')




