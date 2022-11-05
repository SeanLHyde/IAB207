from flask import Blueprint, render_template, request, redirect, url_for
from .models import Events
from .forms import EventForm
from . import db
import os
from werkzeug.utils import secure_filename

events = Blueprint('event', __name__, url_prefix='/events')

@events.route('/event_creation', methods = ['GET', 'POST'])
def create():
  print('Method type: ', request.method)
  form = EventForm()
  if form.validate_on_submit():
    print('Successfully created new event', 'success')
    #return redirect(url_for('event.create'))
  return render_template('events/event_creation.html', form=form)


