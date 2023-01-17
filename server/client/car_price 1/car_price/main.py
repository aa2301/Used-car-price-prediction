from flask import Flask, render_template, request, redirect, url_for, session
# from flask_mysqldb import MySQL
# import MySQLdb.cursors
import re
import requests, json

app = Flask(__name__)

# Change this to your secret key (can be anything, it's for extra protection)
app.secret_key = 'your secret key'

# http://localhost:5000/pythonlogin/ - the following will be our login page, which will use both GET and POST requests
@app.route('/car_price/', methods=['GET', 'POST'])
def home():

    return render_template('crop.html')    

if __name__ == '__main__':
    app.run(debug=True)
