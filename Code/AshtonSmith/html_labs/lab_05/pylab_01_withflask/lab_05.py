from flask import Flask, render_template, redirect, request
import ashton_lab_1 as converter
app = Flask(__name__)




@app.route('/', methods=['GET', 'POST'])
def index():
    print(request.form)
    num = request.form.get("amount")
    if(num == None or num == ''): num = 0
    init_unit = str(request.form.get("init_unit"))
    final_unit = str(request.form.get("final_unit"))
    result = convert(num, init_unit, final_unit)
    print (result)
    return render_template('index.html', result= result)


#convert from unit 1 to unit 2 using lab1 functions
def convert(num, unit_1, unit_2):
    num2 = converter.convert_to_meters(float(num), unit_1)
    return (str(converter.convert_from_meters(float(num2), unit_2)) + " " + str(unit_2))


# @app.route('/<string:name>/<int:id>')
# def profile(name,id):
#     return "hello, " + name + ", your id is: " + str(id)
app.run(debug=True)