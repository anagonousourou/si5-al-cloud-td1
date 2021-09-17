from datetime import datetime
from flask import Flask,request
import os
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

db=SQLAlchemy(app)

#app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SQLALCHEMY_DATABASE_URI']=os.getenv('DB_URI','postgresql://patrick:patrick_pw9@localhost:5432/cloudtd1db')


class Visit(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    client=db.Column(db.String(100))
    date_created= db.Column(db.DateTime, default=datetime.now)

@app.route('/')
def home():
    visit=Visit(client=request.remote_addr)
    print(app.config['SQLALCHEMY_DATABASE_URI'])
    db.session.add(visit)
    db.session.commit()
    return f'Hello client n°{db.session.query(Visit).count()}'