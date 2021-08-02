import math
units = {
        'ft':0.3048,
        'mi':1609.34,
        'm':1,
        'km':1000,
        'yard':0.9144,
        'inch': 0.0254
}

def main():

    while True:
        try:
            distance = int(input("What is the distance? "))
        except:
            print("Error: Distance must be an integer value.")
            continue
        input_units = input("What are the input units? ")
        output_units = input("What are the output units? ")

        converted_units = convert(distance,input_units,output_units,units)
        if converted_units == 0:
            print("Invalid units")
        else:
            print(f"{distance}{input_units} is {round(converted_units,2)}{output_units} ")
            break


    exit()

def convert(distance,input_units,output_units):
    try:
        return distance * units[input_units] * (1/units[output_units])
    except(KeyError):
        return 0

if __name__=='__main__':
    main()