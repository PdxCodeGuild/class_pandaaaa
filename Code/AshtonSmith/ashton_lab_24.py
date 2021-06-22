# Lab 24: Rain Data
# The 'City of Portland Bureau of Environmental Services' operates and maintains a network of rain gauges around Portland, and publishes their data publicly: http://or.water.usgs.gov/non-usgs/bes/

# The data tables available on the site look something like...

# Daily  Hourly data -->

#    Date     Total    0   1
# --------------------------
# 25-MAR-2016     0    0   0
# 24-MAR-2016     6    0   1
# 23-MAR-2016     -    -   -
# MORE...

# Download one of these files and write a function to load the file. The two columns that are most important are the date and the daily total. The simplest representation of this data is a list of tuples, but you may also use a list of dictionaries, or a list of instances of a custom class.

# To parse the dates, use datetime.strptime. This allows for easy access to the year, month, and day as ints. Below I've shown how to parse an example string, resulting in a datetime object. We can then access the year, month, and day on that datetime as ints. Later, if you want to print the datetime in a more human-readable format, you can use datetime.strftime.

# import datetime
# date = datetime.datetime.strptime('25-MAR-2016', '%d-%b-%Y')
# print(date.year)   # 2016
# print(date.month)  # 3
# print(date.day)    # 25
# print(date)  # 2016-03-25 00:00:00
# print(date.strftime('%d-%b-%Y'))  # 25-Mar-2016
# Version 2
# Now that you've successfully extracted the data, let's do some statistics.

# Calculate the mean of the data:

# mean

# Use the mean to calculate the variance:

# variance

# Find the day which had the most rain.

# Find the year which had the most rain on average.

# Version 3
# Using matplotlib create a chart of the dates and the daily totals for a given year. The x_values will be a list of dates, The y_values are a list of the daily totals. If you don't have matplotlib installed, run pip install matplotlib. You can learn more about matplotlib here.

# import matplotlib.pyplot as plt
# ...
# plt.plot(x_values, y_values)
# plt.show()
# Some charts you can make are:

# all the data, date vs daily total
# monthly totals, average across multiple years
# # total yearly rainfall, year by year
import re
import datetime
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
    
    have_date = False
    key = ''
    del my_str_list[0:80]
    
    for i in my_str_list:
        if(len(i) > 3) and i[2] == '-':
            #print(i)
            key = i
            have_date = True
        elif have_date:
    #        print('Rain Fall total:' + i)
            have_date = False
            if i == '-':
                rain_dict[key] = 0
            else:
                rain_dict[key] = int(i)

    #date and amounts sucesfully load into dict
    #need to now search the dict and print the largest day

    max_key = max(rain_dict, key = rain_dict.get) 
    print("The most rain fall occured on: " + str(max_key) + '\nIt rained ' + str(rain_dict[max_key]) + ' inches.')
    curr_key = ''
    for key in rain_dict:
        curr_key = key[-4]+key[-3]+key[-2] +key[-1]
        if curr_key in total_dict:
            total_dict[curr_key] = total_dict[curr_key] + int(rain_dict[key])
        else:
            total_dict[curr_key] = int(rain_dict[key])

    print(total_dict)
    #print(my_str_list[j])
    #each set has 26 items
    #first item [0] = date
    #second item[1] = total
    #[2]-[25] = hourly totals

# x = 0
# length = len(html)
# replacement = ''
# for i in range(length):
#     if html[i]== '-':
#         while x < length-1  and html[x] == '-':
#             x +=1
#         while x < length -1:
#             replacement += html[x]
#             x +=1 
#         break
#     x += 1


main()