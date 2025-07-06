from flask import Flask
from flask_login import LoginManager
from models import db, User

#concepts should be learn:
#crud==> create ,read,update ,delete
#authentification ==> login,logout

def create_app():
    app = Flask(__name__) #__name__ tells Flask where to look for templates, static files, and other resources
    app.config['SECRET_KEY'] = 'secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    #we can connect the database diretelly with the app when we create db like ===> db = SQLAchemy(app)
    db.init_app(app) #connect the database with Flask application method more orginaze

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_login(user_id):
        return User.query.get(int(user_id))

    from main import main as main_blueprint
    app.register_blueprint(main_blueprint) #Registers the main blueprint with the Flask app, for making all routes in main.py available
    from auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    with app.app_context():
        db.create_all() #should be inside the app_context for run and avoid error 
        
    return app #return the app after configure it

#we means by .file_name {. ==> current folder wish we work on it, file_name ==> file wish want import from it}  

    

# Note:there is feature should be know it in the future allow to whole the project without create run.py and direct by special commands
# in this porject we depend on the `foctory desgin pattern`


# config is dictionary in Flask use to store configuration vlaues
# SECRET_KEY: is required for securely signing session cookies and other security-related operations {flash message,CSRF protection,session data}


# {@login_manager.user_loader ==> this the decorator wish the flask-login know the method role by it
#     def load_login(user_id):
#         return User.query.get(int(user_id)) }
# ==> this function called from the flask-login when there is request occur (user login) and its role get the user (object) by its id 
# by this function we can use the current_user whereever in code 