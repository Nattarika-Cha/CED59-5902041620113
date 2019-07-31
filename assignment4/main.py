from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)
@app.route("/")
def index(): #โมดูลรับค่าจากไฟล์ index.html โดยการส่งค่าในรูปแบบ POST
    return render_template('index.html')
@app.route('/home', methods=['POST'])
def save(): #โมดูลแสดงข้อมูล
    return "Complete"
app.run(debug=True)

    