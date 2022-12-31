from flask import Flask, render_template, request
from flask_mail import Mail, Message
import datetime
import smtplib
import requests

OWN_EMAIL = ""
OWN_PASSWORD = ""

app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'josiasfaustinboukan@gmail.com'
app.config['MAIL_PASSWORD'] = 'CCNA@2022'

mail = Mail(app)

@app.route('/home')
def home():
	# update the footer  copyright current year
	current_year = datetime.datetime.now().year
	return render_template("index.html", year=current_year)

@app.route('/contact')
def contact_button():
	return render_template("getintouch.html")

def sendContactForm(result):
    msg = Message("contact form from jzone website", 
        sender="josiasfaustinboukan@gmail.com",
        recipients=["joejosiasb@gmail.com"])

    msg.body = """ 
    Hello there,
    You just received a contact form.

    Name: {}
    Email: {}
    Message: {}

    regards,
    Webmaster

    """.format(result['name'], result['email'], result['message'])

    mail.send(msg)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
       result = {}

       result['name'] = request.form['name']
       result['email'] = request.form['email'].replace(' ', '').lower()
       result['message'] = request.form['message']

       sendContactForm(result)

       return render_template('getintouch.html', **locals())

    return render_template("getintouch.html", ** locals())


# def send_email(name, email, message):
#     email_message = f"Subject:New Message\n Name: {name}\nEmail: {email}\n Message:{message}"
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(OWN_EMAIL, OWN_PASSWORD)
#         connection.sendmail(OWN_EMAIL, email_message)

if __name__=='__main__':
	app.run(debug=True)
	# app.run(debug=False, host='0.0.0.0')