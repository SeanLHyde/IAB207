from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template('index.html')


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

@views.route('/R&B')
def rb():
    return render_template('R&B.html')

@views.route('/afrobeats')
def afrobeats():
    return render_template('afrobeats.html')

@views.route('/cancelled')
def cancelled():
    return render_template('cancelled.html')

@views.route('/drake')
def drake():
    return render_template('drake.html')

@views.route('/burnaboy')
def burnaboy():
    return render_template('burnaboy.html')

@views.route('/wizkid')
def wizkid():
    return render_template('wizkid.html')

@views.route('/lildurk')
def lildurk():
    return render_template('lildurk.html')

@views.route('/kanye')
def kanye():
    return render_template('kanye.html')

@views.route('/savage')
def savage():
    return render_template('savage.html')