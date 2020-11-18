# impoerting modules
from flask import Flask ,render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json
# app name
app=Flask(__name__)
db = SQLAlchemy(app)
# which server iam using
local_server=True
# opening of file json
with open('config.json' , 'r') as c:
    params = json.load(c)["params"]
# chossing server using json
if (local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']
# database model
class fendbeck(db.Model):
    sno=db.Column(db.Integer,primary_key=True) 
    name =db.Column(db.String(15),nullable=False)
    email=db.Column(db.String(25),nullable=False)
    phoneno=db.Column(db.String(12),nullable=True)
    fedback=db.Column(db.String(100),nullable=False)
    date=db.Column(db.String(12), nullable=True)

@app.route("/" , methods=['GET','POST'])
def index():
    if (request.method=='POST'):
        name=request.form.get('name')
        email=request.form.get('email')
        phonenumber=request.form.get('phoneno')
        messsage=request.form.get('message')
        entry=fendbeck(name=name , email=email , phoneno=phonenumber ,date=datetime.now() ,fedback=messsage)
        db.session.add(entry)
        db.session.commit()  
    return render_template('/index.html', params=params)
app.run(debug=True)       