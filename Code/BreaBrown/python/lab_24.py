import datetime as dt

with open("crime_data.csv", "r") as f:
    data = f.read().split('\n')
# print(data)

def c_s_v(parameter):
    c_s_v_list = []
    for line in parameter:
        info = line.split(",")      
        Record_ID = info[0]
        Report_Date = info[1]
        Report_Time = info[2]
        Major_Offense_Type = info[3]
        Address = info[4]
        Neighborhood = info[5]
        Police_Precint = info[6]
        Police_District = info[7]
        X_Coordinate = info[8]
        Y_Coordinate = info[9]
        data = {'Record ID': Record_ID, 'Report Date': Report_Date, 'Report Time': Report_Time, 'Major Offense Type': Major_Offense_Type, 'Address': Address, 'Neighborhood': Neighborhood, 'Police Precinct': Police_Precint, 'Police District': Police_District, 'X Coordinate': X_Coordinate, 'Y Coordinate': Y_Coordinate}
        c_s_v_list.append(data)
    return c_s_v_list


x = c_s_v(data)


def crime_counter(data):
    crime_count = { 
    'total crimes': 0,
    'Larceny': 0,
    'Fraud': 0,
    'Burglary': 0,
    'Trespass': 0,
    'Assault': 0,
    'Vandalism': 0,
    'Disorderly Conduct': 0,
    'Motor Vehicle Theft': 0,
    'Drugs': 0,
    'Arson': 0,
    'Liquor Laws': 0,
    'Robbery': 0,
    'Aggravated Assault': 0,
    'DUII': 0,
    'Forgery': 0,
    'Runaway': 0,
    'Curfew': 0,
    'Stolen Property': 0,
    'Sex Offenses': 0,
    'Weapons': 0,
    'Kidnap': 0,
    'Embezzlement': 0
    }
    for i in data:
        crime_count['total crimes'] += 1
        # print(i)
        # print(i["Major Offense Type"])
        if i['Major Offense Type'] == '"Larceny"':
            crime_count['Larceny'] += 1
        elif i['Major Offense Type'] == '"Fraud"':
            crime_count['Fraud'] += 1
        elif i['Major Offense Type'] == '"Burglary"':
            crime_count['Burglary'] += 1
        elif i['Major Offense Type'] == '"Trespass"':
            crime_count['Trespass'] += 1 
        elif i['Major Offense Type'] == '"Assault':
            crime_count['Assault'] += 1
        elif i['Major Offense Type'] == '"Vandalism"':
            crime_count['Vandalism'] += 1
        elif i['Major Offense Type'] == '"Disorderly Conduct"':
            crime_count['Disorderly Conduct'] += 1
        elif i['Major Offense Type'] == '"Motor Vehicle Theft"':
            crime_count['Motor Vehicle Theft'] += 1
        elif i['Major Offense Type'] == '"Drugs"':
            crime_count['Drugs'] += 1
        elif i['Major Offense Type'] == '"Arson"':
            crime_count['Arson'] += 1
        elif i['Major Offense Type'] == '"Liquor Laws"':
            crime_count['Liquor Laws'] += 1
        elif i['Major Offense Type'] == '"Robbery"':
            crime_count['Robbery'] += 1
        elif i['Major Offense Type'] == '"Aggravated Assault"':
            crime_count['Aggravated Assault'] += 1
        elif i['Major Offense Type'] == '"DUII"':
            crime_count['DUII'] += 1
        elif i['Major Offense Type'] == '"Forgery"':
            crime_count['Forgery'] += 1
        elif i['Major Offense Type'] == '"Runaway"':
            crime_count['Runaway'] += 1
        elif i['Major Offense Type'] == '"Curfew"':
            crime_count['Curfew'] += 1
        elif i['Major Offense Type'] == '"Stolen Property"':
            crime_count['Stolen Property'] += 1
        elif i['Major Offense Type'] == '"Sex Offenses"':
            crime_count['Sex Offenses'] += 1
        elif i['Major Offense Type'] == '"Weapons"':
            crime_count['Weapons'] += 1
        elif i['Major Offense Type'] == '"Kidnap"':
            crime_count['Kidnap'] += 1
        else:
            i['Major Offense Type'] == 'Embezzlement'
            crime_count['Embezzlement'] += 1
    return crime_count
y = crime_counter(x)

# for i in x:
#     year = i['Report Date']
#     print(year.year())

def year_scraper(data):
    count = 0
    for item in data:
        x = item['Report Date']
        x =x[1:-1]
        print(count)
        count += 1 
        try:
            x = dt.datetime.strptime(x, '%m/%d/%Y')
            print(x)
        except:
            x = dt.datetime.now()
        # print(x.year)
year_scraper(x)