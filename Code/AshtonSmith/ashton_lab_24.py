# Lab 24: Rain Data
# The 'City of Portland Bureau of Environmental Services' operates and maintains a network of rain gauges around Portland
# , and publishes their data publicly: http://or.water.usgs.gov/non-usgs/bes/

#this program downloads the rain fall data and stores them in a dictionary, then prints the day with the most rainfall and the year
#with the most rainfall. The program then plots the data on a matplotlib chart (x = year),(y = rain total)
#import re
#import datetime
import matplotlib.pyplot as plt
from urllib.request import urlopen, Request
rain_dict = {
}
total_dict ={
}



def main():
    url = 'https://or.water.usgs.gov/non-usgs/bes/hayden_island.rain'
    request = Request(url)
    response = urlopen(request)
    html_bytes = response.read()
    html = html_bytes.decode('utf-8')
    response.close()
    my_str_list = html.split()
    rain_dict_filler(my_str_list)
    total_calculator()
    print_total_dict()
    data_chart()
    

    
#this function fills the data in the rain dictionary with the string argument
def rain_dict_filler(my_str_list):   
    have_date = False
    key = ''
    del my_str_list[0:80]#data starts after 80
    
    for i in my_str_list:
        if(len(i) > 3) and i[2] == '-':
            key = i
            have_date = True
        elif have_date:
            have_date = False
            if i == '-':
                rain_dict[key] = 0
            else:
                rain_dict[key] = int(i)



#this function calculates rain fall totals by year and stores in in total_dict
def total_calculator():
    max_key = max(rain_dict, key = rain_dict.get) 
    print("The most rain fall occured on: " + str(max_key) + '. It rained ' + str(rain_dict[max_key]) + ' inches.')
    curr_key = ''
    for key in rain_dict:
        curr_key = key[-4]+key[-3]+key[-2] +key[-1]
        if curr_key in total_dict:
            total_dict[curr_key] = total_dict[curr_key] + int(rain_dict[key])
        else:
            total_dict[curr_key] = int(rain_dict[key])



#this function prints the rain fall totals by year
def print_total_dict():
    highest_year_amt = 0
    highest_year = ''
    for key in total_dict:
        if(total_dict[key] > highest_year_amt):
            highest_year = key
    print('The most rain fall occured in ' + str(highest_year) + ', it rained a total of ' + str(total_dict[highest_year]) + ' inches.')



#this function plots the rain data
def data_chart():
    plt.figure('Rain Data', figsize=(16,8))
    plt.plot( list(total_dict.keys()), list(total_dict.values()) )
    plt.title('Historical Rainfall Totals in Portland.')
    plt.xlabel('Year')
    plt.ylabel('Rainfall (in)')
    plt.grid(True)
    plt.gca().invert_xaxis()
    plt.show()


