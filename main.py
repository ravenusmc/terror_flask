#This is the main file for the project.

import pandas as pd
import numpy as np

#importing all files
from flask import Flask, render_template, request
from ideology import *

#Setting up flask
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title='Home Page')

#Code for pages dealing with ideology pages
@app.route('/ideology')
def idea():
    return render_template('idea.html', title='Ideology Page')

@app.route('/right_wing')
def right():
    ideology = Ideology()
    total, right = ideology.right_wing_info()
    return render_template('right.html', title='Right Wing Terrorism Info', total = total, right = right )

@app.route('/left_wing')
def left():
    ideology = Ideology()
    total, left = ideology.left_wing_info()
    return render_template('left.html', title='Left Wing Terrorism Info', total = total, left = left)

@app.route('/islamic')
def ideology():
    ideology = Ideology()
    total, islamic = ideology.islamic_info()
    return render_template('islamic.html', title='Islamic Terrorism Info', total = total, islamic = islamic)

#The following code is for prevented/not prevented attacks.
@app.route('/prevented')
def prev():
    return render_template('prev.html', title='Prevented / Not Prevented')

@app.route('/prev')
def prev_viewing():
    return render_template('prevented.html', title='Prevented')

@app.route('/not_prev')
def not_prev():
    return render_template('not_prev.html', title='Not Prevented')

#This line will actually run the app.
app.run(debug=True)
