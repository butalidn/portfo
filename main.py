import os
import csv
from datetime import datetime
from flask import Flask, render_template, send_from_directory, request, redirect
from Scripts.email_sender import send_email

# had to use '$env:FLASK_APP = "main.py' and 'flask run'

app = Flask(__name__)


@app.route('/<string:page_name>')
def get_page(page_name):
    return render_template(page_name)


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            # send_email(data['email'], data['subject'], data['message'])
            return redirect('thank_you.html')
        except:
            return 'did not save to database'
    else:
        return 'whoops!'


def write_to_file(data):
    with open('database.txt', 'a') as my_file:
        my_file.write(
            f'{data["email"]},{data["subject"]},{data["message"]},{datetime.now().strftime("%m/%d/%Y %H:%M")}\n')


def write_to_csv(data):
    with open('database.csv', 'a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(
            [data['email'], data['subject'], data['message'], datetime.now().strftime("%m/%d/%Y %H:%M")])
#:
# @app.route('/index.html')
# def index():
#     return render_template('index.html')
#
#
# @app.route('/')
# def home():
#     return render_template('index.html')
#
#
# @app.route('/about.html')
# def about():
#     return render_template('about.html')
#
#
# @app.route('/components.html')
# def components():
#     return render_template('components.html')
#
#
# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')
#
#
# @app.route('/work.html')
# def work():
#     return render_template('work.html')
#
#
# @app.route('/works.html')
# def works():
#     return render_template('works.html')
