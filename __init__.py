from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import configure_uploads, IMAGES, UploadSet


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['UPLOADED_IMAGES_DEST'] = 'uploads'


    images =UploadSet('images',IMAGES)
    configure_uploads(app, images)
   

    


    db.init_app(app)


    
    login_manager = LoginManager()
   
    login_manager.init_app(app)
 
    from .models import User

    @app.before_first_request
    def create_table():
        db.create_all()

    
    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))
     
     # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    #--- blueprint for admin
    from .adminMngt import admin as admin_blueprint
    app.register_blueprint(admin_blueprint)

    # blueprint for customer routes and controllers
   
    from .CustMngt import customer as customer_blueprint
    app.register_blueprint(customer_blueprint)

    return app