from flask import Flask
from flask import render_template
from flask import request

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length
from wtforms.fields.html5 import EmailField

import pyodbc
import mysql.connector

login = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  passwd="",
  database="login",
  use_unicode=True,
  charset="utf8"
)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'any secret string'

class LoginForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired(message='Name is required!')])
    surname = StringField('Surname', validators=[InputRequired(message='Surname is required!')])
    email = EmailField('Email', validators=[InputRequired(message='Email is required!')])
    username = StringField('Username', validators=[InputRequired(message='Username is required!')])
    password = PasswordField('Password', validators=[InputRequired(message='Password is required!'), Length(min=8, max=100, message='Please input password more 8 characters')])

@app.route("/form", methods=['GET' , 'POST'])
def form():
    form = LoginForm()
    if form.validate_on_submit():
      name = form.name.data
      surname = form.surname.data
      username = form.username.data
      email = form.email.data
      password = form.password.data

      cursor = login.cursor()
      sql_get = "SELECT * FROM user"
      try:
          cursor.execute(sql_get)
          results = cursor.fetchall()
          # print(cursor)
          # print(results[0])
          for row in results:
              # print("Username =" , row[3])
              # print(username)
              if row[3] == username:
                  data = "Username have ben in database"
                  return render_template('index.html', form=form , data=data)
                  # break
      except:
          print ("Error: unable to fetch data")
          
      cursor = login.cursor()
      sql = '''INSERT INTO user(name, surname, username, email, password)VALUES ('%s','%s','%s','%s','%s')'''% (name, surname, username, email, password)
      try:
          cursor.execute(sql)
          login.commit()
      except:
          login.rollback()
      login.close()
      return "Complete"
    return render_template('index.html', form=form)

# @app.route('/home', methods=['POST'])
# def user():
#     name = request.form['name']
#     surname = request.form['surname']
#     username = request.form['username']
#     email = request.form['email']
#     password = request.form['password']
#     cursor = login.cursor()
#     sql_get = "SELECT username FROM user"
#     try:
#         cursor.execute(sql_get)
#         results = cursor.fetchall()
#         print(results)
#         for row in results:
#             print(row)
#             print(row.strip('('))
#             print(username)
#             if row == username:
#                 print("user same in database")
#                 break
#             # print ("Customer : %s,Tel. : %s" % name, tel)
#     except:
#         print ("Error: unable to fetch data")
#     cursor = login.cursor()
#     sql = '''INSERT INTO user(name, surname, username, email, password)VALUES ('%s','%s','%s','%s','%s')'''% (name, surname, username, email, password)
#     try:
#         cursor.execute(sql)
#         login.commit()
#     except:
#         login.rollback()
#     login.close()
#     return "Complete"
app.run(debug=True)

    