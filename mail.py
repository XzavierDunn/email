import os
import smtplib
import time

emailAdd = os.environ.get('email')
emailPass = os.environ.get('emailPass')

target = input('Who do you want to send an email to? ')

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(emailAdd, emailPass)

    subject = input('Subject: ')
    body = input('Body: ')
    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail(emailAdd, target, msg)
    print(f'Sent')

