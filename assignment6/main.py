from flask import Flask
from flask import render_template
from flask import request
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
@app.route("/")
def index():
    return render_template('index.html')
@app.route('/home', methods=['POST'])
def user():
    name = request.form['name']
    surname = request.form['surname']
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    # cursor = login.cursor()
    # sql_get = "SELECT username FROM user"
    # try:
    #     cursor.execute(sql_get)
    #     results = cursor.fetchall()
    #     print(results)
    #     for row in results:
    #         print(row)
    #         print(row.strip('('))
    #         print(username)
    #         if row == username:
    #             print("user same in database")
    #             break
    #         # print ("Customer : %s,Tel. : %s" % name, tel)
    # except:
    #     print ("Error: unable to fetch data")
    cursor = login.cursor()
    sql = '''INSERT INTO user(name, surname, username, email, password)VALUES ('%s','%s','%s','%s','%s')'''% (name, surname, username, email, password)
    try:
        cursor.execute(sql)
        login.commit()
    except:
        login.rollback()
    login.close()
    return "Complete"
app.run(debug=True)

    