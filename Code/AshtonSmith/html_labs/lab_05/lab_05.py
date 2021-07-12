from flask import Flask, render_template, redirect, request
import ashton_lab_1 as converter
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    print(request.form)
    num = request.form.get("amount")
    init_unit = str(request.form.get("init_unit"))
    final_unit = str(request.form.get("final_unit"))
    result = convert(num, init_unit, final_unit)
    print (result)
    return render_template('index.html')
def convert(num, unit_1, unit_2):
    num2 = converter.convert_to_meters(num, unit_1)
    return (str(converter.convert_from_meters(float(num2), unit_2)) + " " + str(unit_2))


app.run(debug=True)