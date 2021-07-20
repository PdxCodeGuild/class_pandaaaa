# Theo Rowlett
# PDX Code Guild Bootcamp HTML/CSS/Flask lab 5
from flask import Flask, render_template, request
import unit_converter

app = Flask('__name__')

@app.route('/')
def index():
    units = unit_converter.units.keys()
    return render_template('index.html',units=units)
  

@app.route('/convert', methods=['GET','POST'])
def convert():
    if request.method =='POST':
        distance = request.values.get('distance')
        input_units = request.values.get('input_units')
        output_units = request.values.get('output_units')
        final_distance = unit_converter.convert(int(distance),input_units,output_units)
        return render_template('convert.html',distance = distance, input_units = input_units, output_units = output_units, final_distance=final_distance)
    else:
        units = unit_converter.units.keys()
        return render_template('index.html',units=units)
        
# THIS HAS TO BE AT THE BOTTOM OF ALL FUNCTIONS!!!!
app.run(debug=True)

if __name__=='__main__':
    index()