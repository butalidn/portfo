import smtplib
import sys
from email.message import EmailMessage
from string import Template
from pathlib import Path


# input = sys.argv[1]
#
# html = Template(Path('index.html').read_text())
# email = EmailMessage()
# email['from'] = 'your sEcrEt admIreR!'
# email['to'] = 'k8twin9966@gmail.com'
# email['subject'] = 'hey there girlie'
#
# email.set_content(html.substitute({'input_text': input}), 'html')
#
# with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.login('balut.tester945@gmail.com', 'mrnixthtester')
#     smtp.send_message(email)
#     print('Email sent!')

def send_email(from_email, subject, message):
    email = EmailMessage()
    email['from'] = "Nik's Website Notifier"
    email['to'] = 'nik.butalid@pop.belmont.edu'
    email['subject'] = subject

    email.set_content(f'Hello, you just received a message from Nik\'s website.\n\n{from_email} said:\n"{message}"')

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('balut.tester945@gmail.com', 'mrnixthtester')
        smtp.send_message(email)
        print('Email sent!')
