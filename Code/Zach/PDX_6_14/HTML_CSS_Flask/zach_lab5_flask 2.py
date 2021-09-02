from flask import Flask, render_template, request, redirect
from flask.helpers import url_for
from werkzeug.utils import redirect

app = Flask(__name__)

@app.route('/hello')
def index(): 
    return 'hello wold'

@app.route('/converter', methods=['GET','POST'])
def converter():
    unit_converter_additional = {
        "ft" : 0.3048,
        "mi" : 1609.34,
        "m" : 1,
        "km" : 1000,
        "yd" : 0.9144,
        "in" : 0.0254,
    }
    converted = "You haven't converted anything yet"
    distance = 0
    units = "m"
    new_units = "mi"
    if request.method=="POST":
        distance = int(request.form['distance'])
        units = str(request.form['units'])
        new_units = str(request.form['new_units'])
        converted = f"{distance} {units} is equal to {round((distance*unit_converter_additional[units])/unit_converter_additional[new_units], 4)} {new_units}!"
    return render_template('zach_lab5_flask.html', distance=distance, units=units, new_units=new_units, converted=converted)

@app.route('/receive_form/', methods=['POST'])
def temperature():
    unit_converter_additional = {
        "ft" : 0.3048,
        "mi" : 1609.34,
        "m" : 1,
        "km" : 1000,
        "yd" : 0.9144,
        "in" : 0.0254
    }
    if request.method=="POST":
        distance = int(request.form['distance'])
        units = str(request.form['units'])
        new_units = str(request.form['new_units'])
        converted = f'{distance} {units} is equal to {round((distance*unit_converter_additional[units])/unit_converter_additional[new_units], 4)} {new_units}!'
    return redirect('/', converted)

app.run(debug=True)