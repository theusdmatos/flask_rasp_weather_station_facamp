import sys
import time
import pyrebase
from random import randint
from flask import Flask, render_template, request

config = {
    "apiKey": "AIzaSyCn4QYDd-5mRT-BXiAVzmXiwhPuT8VeGVU",
    "authDomain": "estacao-ca5e5.firebaseapp.com",
    "databaseURL": "https://estacao-ca5e5-default-rtdb.firebaseio.com/",
    "storageBucket": "estacao-ca5e5.appspot.com",
}

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def weather():

    firebase = pyrebase.initialize_app(config)
    auth = firebase.auth()
    user = auth.sign_in_with_email_and_password(
        'rasp170706@gmail.com',
        '159Senha'
    )

    data = firebase.database()
    dbTemp = data.child("Temperatura").get(user['idToken'])
    dbHumi = data.child("Umidade").get(user['idToken'])
    print(dbTemp.val())
    print(dbHumi.val())

    temp = dbTemp.val()
    hum = dbHumi.val()

    return render_template('index.html', temp=temp, hum=hum)


if __name__ == '__main__':
    app.run(debug=True)
