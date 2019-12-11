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
    for i in range(500):
        counter += 1
        subject = f'Chore {counter}'
        body = '''
Hello 


How are you doing? I am in an important conference right now, and i
need some certain task to be carry out by you Asap kindly drop me your
cell # to text you on immediately thank you.


Thanks, Scott Jones

Founder, Chairman, President at Eleven Fifty Academy

sent from iPhone

        '''
        msg = f'Subject: {subject}\n\n{body}'

        smtp.sendmail(emailAdd, target, msg)
        print(f'Sent {counter}')
        time.sleep(3)

