'''
lab24: rain data | version 3
'''
import datetime
import string
import matplotlib.pyplot as plt

rain_data = "mt_tabor_rain.txt"
dict_rain_data = {}

def parse_data():
    with open(rain_data, "r") as rain_data_string:
        line = rain_data_string.readlines()
        #parse date and total rain fall
        for n in range(11, len(line)):
            line_string = line[n]
            # print(line_string)
            rain_count = line_string[14:17].replace(" ", "")
            # print(rain_count)
            if rain_count[0] in string.digits:
                rain_count = int(rain_count)
                dict_rain_data[line_string[0:11]] = rain_count #parse date and total rain fall into a dictionary
    
    print(dict_rain_data)


def calculate_mean():
    sum = 0
    count = 0
    print(dict_rain_data)
    for n in dict_rain_data:
        sum += dict_rain_data[n]
        count += 1
    return (sum/count), count

def calculate_variance(mean, count):
    sum = 0
    for n in dict_rain_data:
        sum += (dict_rain_data[n] - mean)**2
    return sum/count

def most_rain_in_one_day():
    max_rain = 0
    max_rain_date = ""
    for n in dict_rain_data:
        if dict_rain_data[n] > max_rain:
            max_rain = dict_rain_data[n]
            max_rain_date = n
    return max_rain, max_rain_date

def calculate_year_with_most_rain():
    dict_year = {}
    sum = 0 
    current_year = 0
    for n in dict_rain_data:
        date = datetime.datetime.strptime(n, '%d-%b-%Y')
        if date.year != current_year or n == "26-AUG-1998":
            dict_year[current_year] = sum
            current_year = date.year
            sum = 0
        sum += dict_rain_data[n]

    max_rain = 0
    year_with_max_rain = ""
    for n in dict_year: # find year that has highest rain
        if dict_year[n] > max_rain:
            max_rain = dict_year[n]
            year_with_max_rain = n
    return max_rain, year_with_max_rain
            
def display_result(mean, count, variance, one_day_high, date, max_rain_by_year, year):
    print(f"The mean of the rain data is {mean} based on a total of {count} days.")
    print(f"The variance of the rain data is {variance}")
    print(f"On {date}, it has the most rain, {one_day_high}.")
    print(f"Year {year} has the highest rain fall of {max_rain_by_year}.")

def plot():
    user_input = input("Enter the year that you would like to see a plot of rainfall by month (e.g. 1998): ")
    sum = 0
    current_month = ""
    
    for n in dict_rain_data: 
        date = datetime.datetime.strptime(n, '%d-%b-%Y')
        if str(date.year) == user_input:
            if str(date.month) != current_month:
                plt.plot(current_month, sum, "ro")
                current_month = (date.month)
                sum = 0
            sum += dict_rain_data[n]
            

    plt.axis([0, 15, 0, 45])
    plt.show()

def main():
    parse_data()
    # mean, count = calculate_mean()
    # variance = calculate_variance(mean, count)
    # one_day_high, date = most_rain_in_one_day()
    # max_rain_by_year, year = calculate_year_with_most_rain()
    # display_result(mean, count, variance, one_day_high, date, max_rain_by_year, year)
    # plot()


main()
