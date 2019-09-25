import os
import smtplib
import time

emailAdd = os.environ.get('email')
emailPass = os.environ.get('emailPass')

target = ''

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(emailAdd, emailPass)

    counter = 0
    for i in range(10001):
        counter += 1
        subject = f''
        body = ''
        msg = f'Subject: {subject}\n\n{body}'

        smtp.sendmail(emailAdd, target, msg)
        print(f'Sent {counter}')
        time.sleep(3)

