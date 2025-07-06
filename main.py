from flask import Blueprint,render_template,request,redirect,flash,url_for
from flask_login import login_required,current_user
from models import Workout,User,db

main = Blueprint('main',__name__)

#the blueprint in flask is methods allow to organize the project into reuseble component for make them easy to mantain separate the logic part on the markub
#Blueprints don't automatically give access to all parts of your Flask app. Instead, they help you structure your app into logical parts (modules), then connect them to the main application 

@main.route('/')
def index():
    return render_template('index.html',
                           filestyle='indexstyle.css',
                           pageTitle="Index Page",
                           checkUserLogin=current_user)

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html',
                           filestyle='profilestyle.css',
                           pageTitle="Profile Page",
                           name=current_user.UserName)

@main.route('/new')
@login_required
def new_workout():
    return render_template('create_workout.html')

@main.route('/new',methods=['POST'])
@login_required
def new_workout_post():
    pushups = request.form.get('pushups')
    comment = request.form.get('comment')

    workout = Workout(pushups=pushups,comment=comment,user_id=current_user.id)
    db.session.add(workout)
    db.session.commit()

    flash("Your workout has been added.")
    # this method use to send message demonstrate result of specific action 
    # and Stored temporarily in the session && utomatically removed after being read once

    return redirect(url_for('main.user_workouts'))

@main.route('/all')
def user_workouts():
    # user = User.query.filter_by(email=current_user.email).first_or_404()
    # workouts = user.workouts
    # print(workouts)
    # return render_template('all_workouts.html',filestyle='all_workouts.css',workouts=workouts,user=user)
    page = request.args.get('page',1,type=int)
    user = User.query.filter_by(email=current_user.email).first_or_404()            
    workouts = Workout.query.filter_by(author=user).paginate(page=page,per_page=3)
    return render_template('all_workouts.html',filestyle='all_workouts.css',workouts=workouts,user=user)



@main.route('/workout/<int:workout_id>/update',methods=['GET','POST'])
@login_required
def update_workout(workout_id):

    workout = Workout.query.get(workout_id)
    if request.method == 'POST':
     workout.pushups =  request.form['pushups']
     workout.comment = request.form['comment']
     db.session.commit()
     flash("Your Workout is updated")
     return redirect(url_for('main.user_workouts'))
    return render_template('Edit_workout.html',workout=workout); 

@main.route('/workout/<int:workout_id>/delete',methods=['GET','POST'])
@login_required
def delete_workout(workout_id):
    workout = Workout.query.get(workout_id)
    db.session.delete(workout)  
    db.session.commit()
    flash("Your Workout is deleted")
    return redirect(url_for('main.user_workouts')) 


#pagination:
# what this line is means ==> page = request.args.get('page', 1, type=int):
# request.args:
# This is a Flask object that contains the query parameters from the URL (the part after the ? in a URL).
# .get('page', 1, type=int):
# 'page': The name of the query parameter you want to get from the URL (e.g., /workouts?page=2).
# 1: The default value if 'page' is not provided in the URL (so if the user visits /workouts with no ?page=, it will use page 1).
# type=int: Converts the value to an integer (so '2' becomes 2).
# return number of page passed as parameter 


# How Pagination Works
# Client requests a page (e.g., /workouts?page=2).
# Server calculates which records to show based on the page number and page size (e.g., 10 per page).
# Server returns only those records and information about total pages, next/previous links, etc.
