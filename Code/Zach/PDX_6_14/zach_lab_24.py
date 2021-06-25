#Zach Watts
#Lab 24: Rain Data

def main():
    date, rainfall = dataset()
    max_rain = max_rainfall(date, rainfall)
    exit()

def dataset():
    date = []
    rainfall = []
    date_dict = {}
    with open('rain.txt', 'r') as file:
        for line in file:
            date.append(line[0:11])
            rainfall.append(line[16])
            for j in file:
                date_dict[line[0:11]] = j[17]
    print(date_dict)
    return date, rainfall

def max_rainfall(date_, rainfall_):
    most_rain = 0
    for day, rain in zip(date_, rainfall_):
        most_rain = day(max(rainfall_))
    print(most_rain)
    return most_rain

main()