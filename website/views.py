
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from .models import Events
from .forms import EventForm, CommentForm
from . import db
import os
from werkzeug.utils import secure_filename
from flask_bootstrap import Bootstrap


views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template('index.html', user=current_user)


@views.route('/user_booking')
def userBooking():
    return render_template('user_booking.html', user=current_user)

@views.route('/hiphop')
def hipHop():
    return render_template('hiphop.html',user=current_user)

@views.route('/event_detail')
def eventDetails():
    return render_template('event_detail.html',user=current_user)

@views.route('/<id>')
def show(id):
    event = Events.query.filter_by(id=id).first()
    # create the comment form
    cform = CommentForm()    
    return render_template('event/displayevent.html', event=event, form=cform, user=current_user)


@views.route('/event_creation', methods = ['GET', 'POST'])
#@login_required
def create():
  print('Method type: ', request.method)
  form = EventForm()
  if request.method == 'POST':
    #call the function that checks and returns image
    #db_file_path=check_upload_file(form)
    event= Events(eventname=form.eventname.data, description=form.description.data, 
    location = form.location.data, date = form.date.data, ticketamount = form.ticketamount.data, 
    ticketprice = form.ticketprice.data, creatorname=form.creatorname.data,  image=form.image.data,)
    # add the object to the db session
    db.session.add(event)
    # commit to the database
    db.session.commit()
    print('Successfully created new event', 'success')
    #Always end with redirect when form is valid
    flash('Successfully created an event', category='success')
    return redirect(url_for('views.home'))
    
  else:
    flash('Error creating event', category='error')
  return render_template('event_creation.html', form=form, user=current_user)


# Function for storing image data correctly but doesn't currently work
# def check_upload_file(form):
#   #get file data from form  
#   fp=form.image.data
#   filename=fp.filename
#   #get the current path of the module file… store image file relative to this path  
#   BASE_PATH=os.path.dirname(__file__)
#   #upload file location – directory of this file/static/image
#   upload_path=os.path.join(BASE_PATH,'static/image',secure_filename(filename))
#   #store relative path in DB as image location in HTML is relative
#   db_upload_path='/static/image/' + secure_filename(filename)
#   #save the file and return the db upload path  
#   fp.save(upload_path)
#   return db_upload_path
