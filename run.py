from __init__ import create_app


app = create_app() #get the configured app (app become access to all blueprint so to all links)

if(__name__ =="__main__"):
  app.run(debug=True)



#should be install the flask-login library to handle the users login
#and for use it and connect with flask application and flask-login should be import and use the class LoginManager {is class part from flask-login}

# advantage keys to LoginManger:
# What is LoginManager?

# LoginManager is a class provided by the flask_login library that helps manage user sessions, such as:

#     Logging users in and out

#     Protecting routes (@login_required)

#     Remembering users across sessions

#     Redirecting to the login page if a user is not authenticated


#~\Documents\LearnPython\learn_flask_full_course\.venv\Scripts\python.exe
