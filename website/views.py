from flask import Flask, Blueprint, render_template, request, url_for
from flask_wtf import FlaskForm
from wtforms import SubmitField, EmailField, SelectField, StringField, TextAreaField
from wtforms.validators import DataRequired, Email

import smtplib
import os


dustin_email = "dustins.webs@gmail.com"
dustin_pw = "lskc oaco ebrg aepe"


class ContactForm(FlaskForm):
    subject = SelectField(choices=['Website', 'Design', 'Other'])
    first_name = StringField(validators=[DataRequired()])
    last_name = StringField()
    email = EmailField(validators=[DataRequired(), Email(message="Please enter a valid email.")])
    text = TextAreaField(validators=[DataRequired()])
    submit = SubmitField("Submit")
 
views = Blueprint('views', __name__)


# Routes

@views.route('/')
def home():
    title = "Home"
    return render_template('home.html', title=title)

@views.route('/services', methods=['GET'])
def services():
    title = "Services"
    return render_template('services.html', title=title)

@views.route('/portfolio', methods=['GET'])
def portfolio():
    title = "portfolio"
    return render_template('portfolio.html', title=title)
    
@views.route('/contact', methods=['POST', 'GET'])
def contact():
    title = "Contact"
#    subject = 'Bible'
#    first_name = None
#    last_name = None
#    email = None
#    text = None

    contact = ContactForm()
    # Validate Forms


    if contact.validate_on_submit():
        subject = contact.subject.data
        first_name = contact.first_name.data
        contact.first_name.data = ''
        last_name = contact.last_name.data
        contact.last_name.data = ''
        email = contact.email.data
        contact.email.data = ''
        text = contact.text.data
        contact.text.data = ''
    return render_template('contact.html', title=title, contact=contact)

@views.route('/thank-you', methods=['POST'])
def thank_you():
    subject = request.form.get("subject")
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")
    message = request.form.get("text")

    response_message = "Thank you for contacting me."
    message_to_me = ("name: " + first_name + " " + last_name) + ("\nemail: " + email) + ("\nmessage: " + message)
    email_to_me = 'Subject: {}\n\n{}'.format(subject, message_to_me)

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(dustin_email, dustin_pw)
    server.sendmail(dustin_email, email, response_message)
    server.sendmail(dustin_email,
                    dustin_email, email_to_me)

    title = "Thank You"
    return render_template('thank_you.html', title=title, subject=subject, first_name=first_name, last_name=last_name,
                           email=email, message=message)