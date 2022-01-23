import os
import csv
from datetime import datetime
from flask import Flask, render_template, send_from_directory, request, redirect
from sqlalchemy.testing.schema import Table

from email_sender import send_email
import pyodbc
import sqlalchemy as sal
from sqlalchemy import create_engine, MetaData, insert
import pandas as pd

# had to use '$env:FLASK_APP = "main.py' and 'flask run'

app = Flask(__name__)


@app.route('/<string:page_name>')
def get_page(page_name):
    return render_template(page_name)


@app.route('/')
def home_page():
    # send_sql_query()
    return render_template('index.html')


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            send_sql_query(data)
            send_email(data['email'], data['subject'], data['message'])
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


def send_sql_query(data):
    Server = "DESKTOP-O22NV3Q\SQLEXPRESS"
    Database = "AdventureWorksLT2019"
    User = "sa"
    Password = "nikolas1"
    Port = "1433"
    user_email = data['email']
    user_subject = data['subject']
    user_message = data['message']
    user_time = datetime.now().strftime("%m/%d/%Y %I:%M %p")

    engine = create_engine(
        f"mssql+pyodbc://{User}:{Password}@{Server}:{Port}/{Database}?driver=ODBC+Driver+17+for+SQL+Server")

    metadata_obj = MetaData()
    example_table = Table("Website", metadata_obj, autoload_with=engine)
    stmt = insert(example_table).values(email=user_email, subject=user_subject,
                                        message=user_message, time=user_time)

    with engine.connect() as conn:
        conn.execute(stmt)
