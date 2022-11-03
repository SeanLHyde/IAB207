from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template('index.html', user=current_user)


@views.route('/user_booking')
def userBooking():
    return render_template('user_booking.html')

@views.route('/event_creation')
def eventCreation():
    return render_template('event_creation.html')

@views.route('/hiphop')
def hipHop():
    return render_template('hiphop.html')

@views.route('/event_detail')
def eventDetails():
    return render_template('event_detail.html')
