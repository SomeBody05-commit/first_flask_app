from flask import Blueprint,render_template,url_for,request,redirect
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user,logout_user,login_required
from models import db,User             

auth = Blueprint("auth",__name__)#create instance from Blueprint class
#the "auth" parameter is The name of the blueprint (used for URL generation and debugging)
#the __name__ is the name of current module

@auth.route('/signup')
def signup():
    return render_template('signup.html',
                           filestyle='signupstyle.css',
                           pageTitle="sign Up Page")

@auth.route('/signup',methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    print(email,password,name,sep=" | ")

    user = User.query.filter_by(email=email).first()

    if user:
      return redirect(url_for('auth.login'))

    new_User = User(email=email,UserName=name,password=generate_password_hash(password,method='pbkdf2:sha256'))  
    db.session.add(new_User)
    db.session.commit()     

    return redirect(url_for('auth.login'))

@auth.route('/login')
def login():
    return render_template('login.html',
                           filestyle='loginstyle.css',
                           pageTitle="login Page")

@auth.route('/login',methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    user = User.query.filter_by(email=email).first()

    if user and check_password_hash(user.password,password):
        login_user(user,remember=remember)
        return redirect(url_for('main.profile'))
    else:
        return redirect(url_for('auth.login'))
    

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))


    

# login_user() is a function provided by Flask-Login that handles the actual user login process. Here's what each part does:
# 1. user - The user object to log in
# This is the User model instance that was found in the database
# It contains all the user's information (id, username, email, etc.)
# Flask-Login will use this to set up the current user session

# 2. remember=remember - The "Remember Me" functionality
# remember is a boolean variable (True or False)
# If True: The user stays logged in even after closing the browser
# If False: The user will be logged out when the browser session ends
#-before execution this function current_user value was None and after execution
# will contain user object of user logged in so will be can access to its info



#request ==> what the client(browser) send to server(flask app here)
#response ==> what the server(flask app) repply to client after processing the request (on form of json data or webpage) and every one has response status code


#we means by third-party term the libraries and packages wish we install them and that created by other creator of flask framework