import string
import datetime

def main():
    data = '..\..\Data\crime_incident_data_recent.csv'
    raw_data = file_io(data)
    arrest_record = parse_data(raw_data)
    print(f"Highest year of recorded crime:\t{highest_year(arrest_record['report_date'])}")
    common_crime(arrest_record['offense_type'])
    exit()

def file_io(filename):
    try:
        f = open(filename)
    except IOError:
        print(f'{filename} unavailable. Exiting application.')
        exit()
    crime_data = f.read()
    f.close()
    return crime_data

def parse_data(raw_data):
    arrest_record = {
        'record_ID': [],
        'report_date': [],
        'report_time': [],
        'offense_type': [],
        'address': [],
        'neighborhood': [],
        'precinct': [],
        'district': [],
        'x': [],
        'y': []
    }
    crimes = raw_data.split('\n')
    for i in range(1,len(crimes)):
        try:
            arrest = crimes[i].split(',')
            for i in range(len(arrest)):
                arrest[i] = arrest[i][1:-1]            
            arrest_record['record_ID'].append(int(arrest[0]))
            arrest_record['report_date'].append(datetime.datetime.strptime(arrest[1], '%m/%d/%Y'))
            arrest_record['report_time'].append(datetime.datetime.strptime(arrest[2], '%H:%M:%S'))
            arrest_record['offense_type'].append(arrest[3])
            arrest_record['address'].append(arrest[4]+arrest[5]+arrest[6])
            arrest_record['neighborhood'].append(arrest[7])
            arrest_record['precinct'].append(arrest[8])
            arrest_record['district'].append(arrest[9])
            try:
                arrest_record['x'].append(float(arrest[10]))
                arrest_record['y'].append(float(arrest[11]))
            except ValueError:
                #No co-ordinates provided, appending 0.00
                arrest_record['x'].append(0.00)
                arrest_record['y'].append(0.00)
        except:
            #Do Nothing, this is null data I don't want to append
            pass
        
    return arrest_record

def highest_year(years):
    highest_crime = 0
    highest_year = 0
    offset = 2014
    span = datetime.datetime.today().year+1-offset
    years_list = [*range(offset,datetime.datetime.today().year+1)]
    count = [*range(0,span)]
    for i in range(len(count)):
        count[i]=0
    for i in range(len(years)):
        count[years_list.index(years[i].year)] += 1
    
    #print("Year\tTotal Crimes")
    for i in range(len(years_list)):
        if count[i] >= highest_crime:
            highest_year = years_list[i]
            highest_crime = count[i]
        #print(f"{years_list[i]}:\t{count[i]}")
    return highest_year

def common_crime(offense_type):
    total_crime = {
        common_offenses : [],
        count : []
    }
    for i in range(len(offense_type)):
        j = offense_compare(offense_type[i],total_crime['common_offenses'])
        if j == -1:
            total_crime['common_offenses'].append(offense_type[i])
            total_crime['count'].append(1)
        else:
            count[j] += 1
    for i in range(len(total_crime['common_offenses'])):
        print(f'{total_crime['common_offenses'][i]}\n{count[i]}\n')

def offense_compare(offense,common_offenses):
    for i in range(len(common_offenses)):
        if offense == common_offenses[i]:
            return i    
    return -1

main()