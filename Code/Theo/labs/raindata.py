import datetime

def main():
    filename='columbia_ips.rain'
    rain_data = openfile(filename)
    #print(rain_data)
    dates = parse_date(rain_data)
    rain_total = parse_total(rain_data)
    #print(type(rain_total[0]))
    highest_index = highest_rain(rain_total)
    print(f'The highest recorded rainfall was {rain_total[highest_index]}" on {dates[highest_index].strftime("%d-%b-%Y")}.')
    annual_average(dates,rain_total)

    exit()

def openfile(filename):
    try:
        f = open(filename)
    except IOError:
        print(f'{filename} unavailable. Exiting application.')
        exit()
    rain_data = f.read()
    f.close()
    return rain_data

def parse_date(rain_data):
    dates = []
    rain_list = rain_data.split('\n')
    for i in range(len(rain_list)):
        datestring = str(rain_list[i]).split()[0]
        dates.append(datetime.datetime.strptime(datestring, '%d-%b-%Y'))
    return dates

def parse_total(rain_data):
    rain_total = []
    rain_list = rain_data.split('\n')
    for i in range(len(rain_list)):
        try:
            rain_total.append(int(rain_list[i].split()[1]))
        except ValueError:
            rain_total.append(0)
    #print(rain_total)
    return rain_total

def highest_rain(rain_total):
    index = 0
    highest = 0    
    for i in range(len(rain_total)-1):
        if rain_total[i] > highest:
            index = i
            highest = rain_total[i]
    return index

def annual_average(dates,rain_total):
    this_year = datetime.datetime.today().year
    offset = 1999
    average_rainfall = {
        'years':[*range(offset,this_year+1)],
        'count':[*range(0,this_year+1-offset)],
        'total':[*range(0,this_year+1-offset)],
        'average':[*range(0,this_year+1-offset)]
    }
    for i in range(len(dates)):
        average_rainfall['count'][dates[i].year-offset] += 1
        average_rainfall['total'][dates[i].year-offset] += rain_total[i]
    
    print("Annual averages:")
    for i in range(len(average_rainfall['years'])):
        try:
            average_rainfall['average'][i] = average_rainfall['count'][i]/average_rainfall['total'][i]
        except ZeroDivisionError:
            average_rainfall['average'][i] = 0
        print(f"{average_rainfall['years'][i]}: {round(average_rainfall['average'][i],4)}\" per day")
    return None




main()