#Zach Watts
#Lab 24: Rain Data

import matplotlib.pyplot as plt

def main():
    date, rainfall, date_dict = dataset()
    max_rain = max_rainfall(date, rainfall, date_dict)
    avg_dict = max_avg_rain(date, rainfall, date_dict)
    ploot(avg_dict)
    exit()

def dataset():
    date = []
    rainfall = []
    date_dict = {}
    with open('rain.txt', 'r') as file:
        for line in file:
            date.append(line[0:11])
            try: rainfall.append(int(line[13:18]))
            except:
                ValueError
                rainfall.append(0)
            try: date_dict[line[0:11]] = int(line[13:18])
            except:
                ValueError
                date_dict[line[0:11]] = 0
    for value in date_dict.values():
        if value == '-':
            value = 0
    return date, rainfall, date_dict

#--------------------------------------------------VERSION 2----------------------------------------------------------#

def max_rainfall(date_, rainfall_, date_dict_):
    most_rain_ = max(rainfall_)
    most_rain_idx = rainfall_.index(most_rain_)
    most_rain_day = date_[most_rain_idx]
    print(f'The most rain in a day took place on {most_rain_day} with {most_rain_*0.01} inches')
    return most_rain_day, most_rain_

def max_avg_rain(date_, rainfall_, date_dict_):
    lst_2021 = []
    lst_2020 = []
    lst_2019 = []
    lst_2018 = []
    lst_2017 = []
    lst_2016 = []
    lst_2015 = []
    lst_2014 = []
    lst_2013 = []
    lst_2012 = []
    lst_2011 = []
    for k, v in date_dict_.items():
        if k[7:11] == '2021':
            lst_2021.append(v)
        elif k[7:11] == '2020':
            lst_2020.append(v)
        elif k[7:11] == '2019':
            lst_2019.append(v)
        elif k[7:11] == '2018':
            lst_2018.append(v)
        elif k[7:11] == '2017':
            lst_2017.append(v)
        elif k[7:11] == '2016':
            lst_2016.append(v)
        elif k[7:11] == '2015':
            lst_2015.append(v)
        elif k[7:11] == '2014':
            lst_2014.append(v)
        elif k[7:11] == '2013':
            lst_2013.append(v)
        elif k[7:11] == '2012':
            lst_2012.append(v)
        elif k[7:11] == '2011':
            lst_2011.append(v)
    avg_2021 = sum(lst_2021)/len(lst_2021)
    avg_2020 = sum(lst_2020)/len(lst_2020)
    avg_2019 = sum(lst_2019)/len(lst_2019)
    avg_2018 = sum(lst_2018)/len(lst_2018)
    avg_2017 = sum(lst_2017)/len(lst_2017)
    avg_2016 = sum(lst_2016)/len(lst_2016)
    avg_2015 = sum(lst_2015)/len(lst_2015)
    avg_2014 = sum(lst_2014)/len(lst_2014)
    avg_2013 = sum(lst_2013)/len(lst_2013)
    avg_2012 = sum(lst_2012)/len(lst_2012)
    avg_2011 = sum(lst_2011)/len(lst_2011)
    lst_of_avgs = [avg_2011, avg_2012, avg_2013, avg_2014, avg_2015, avg_2016, avg_2017, avg_2018, avg_2019, avg_2020, avg_2021]
    avg_dict = {
        avg_2011 : 2011,
        avg_2012 : 2012,
        avg_2013 : 2013,
        avg_2014 : 2014,
        avg_2015 : 2015,
        avg_2016 : 2016,
        avg_2017 : 2017,
        avg_2018 : 2018,
        avg_2019 : 2019,
        avg_2020 : 2020,
        avg_2021 : 2021
    }
    highest_yearly_rain = max(lst_of_avgs)
    print(f'The year with the highest daily average rainfall took place in {avg_dict[highest_yearly_rain]} with {round(highest_yearly_rain, 2)*0.01} inches.')
    return avg_dict
#------------------------------------------------------------VERSION 3---------------------------------------------------------#

def ploot(avg_dict_):
    plt.plot(avg_dict)
    pass
        


main()