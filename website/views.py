
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from .models import Events, Comments
from .forms import EventForm, CommentsForm
from . import db
import os
from werkzeug.utils import secure_filename
from flask_bootstrap import Bootstrap


views = Blueprint('views', __name__)

#Home route which redirects to index.html
@views.route('/')
def home():
    events = Events.query.all()
    print(events[0].eventname)
    return render_template('index.html', user=current_user, event=events)

#Not implemented, basic html
@views.route('/user_booking')
def userBooking():
    return render_template('user_booking.html', user=current_user)

#Displays the details of the event based on the primary key "ID" in the database
@views.route('event_detail/<id>')
def show(id):
    events = Events.query.filter_by(id=id).first()
    # create the comment form
    cform = CommentsForm()    

    return render_template('event_detail.html', event=events, form=cform, user=current_user)

@views.route('event_detail/<id>/booking', methods=['GET', 'POST'])
@login_required
def book(id):
  print("step")
  amount = request.form.get("quantity")
  print(amount)
  avaliable = Events.query.filter_by(id=id).first()
  print(avaliable.ticketamount)
  if not amount:
    flash("Please select amount of tickets", category= 'error')
  elif amount > avaliable.ticketamount:  
    flash("Not enough tickets avalaible", category = 'error')
  else:
    flash("Tickets successfully booked", category = 'success')
    return render_template('event_detail.html', event=avaliable, user=current_user)
  return render_template('event/displayevent.html', events=event, form=form, user=current_user)


#Route to create an event
#Uses @loging_required to ensure only authenticated users can get to this page & create an even
@views.route('/event_creation', methods = ['GET', 'POST'])
@login_required
def create():
  print('Method type: ', request.method)
  form = EventForm()
  if request.method == 'POST':
    if not form.eventname.data:
      flash('Error creating event', category='error')
    else:
      #call the function that checks and returns image
      # db_file_path=check_upload_file(form)
      event= Events(eventname=form.eventname.data, description=form.description.data, 
      location = form.location.data, date = form.date.data, ticketamount = form.ticketamount.data, 
      ticketprice = form.ticketprice.data, status =form.status.data, creatorname=form.creatorname.data,  image=form.image.data)
      # add the object to the db session
      db.session.add(event)
      # commit to the database
      db.session.commit()
      print('Successfully created new event', 'success')
      #Always end with redirect when form is valid
      flash('Successfully created an event', category='success')
      return redirect(url_for('views.home'))
  return render_template('event_creation.html', form=form, user=current_user)

#Route to post a comment
#As soon as the comment is posted, it redirects them to /post-comment/<events_id> & then redirects them back
#to the event page & shows the new comment
@views.route('/post-comment/<events_id>', methods=['POST'])
@login_required
def post_comment(events_id):
    comment = request.form.get('comment')

    if not comment:
        flash('You cannot post an empty comment')
    else:
        comment = Comments(comment=comment, events_id=events_id)
        db.session.add(comment)
        db.session.commit()
        print('yes')
    return redirect(url_for('views.show', id=events_id))

#Function for the search feature to search via description
@views.route('/search')
def search():
    if request.args and "search" in request.args:
        print(request.args['search'])
        searchstring = "%" + request.args['search'] + '%'
        events = Events.query.filter(Events.description.like(searchstring)).all()
        return render_template('index.html', event=events, user=current_user)
    else:
        return redirect(url_for('main.index', user=current_user))



# Function for storing image data correctly but doesn't currently work
def check_upload_file(form):
  #get file data from form  
  fp=form.image.data
  filename=fp.filename
  #get the current path of the module file… store image file relative to this path  
  BASE_PATH=os.path.dirname(__file__)
  #upload file location – directory of this file/static/image
  upload_path=os.path.join(BASE_PATH,'static/image',secure_filename(filename))
  #store relative path in DB as image location in HTML is relative
  db_upload_path='/static/image/' + secure_filename(filename)
  #save the file and return the db upload path  
  fp.save(upload_path)
  return db_upload_path

  
