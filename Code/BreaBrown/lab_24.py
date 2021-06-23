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
print(x)


def crime_counter(data):
    crime_count = { 
    'total crimes': 0,
    'larceny': 0,
    'fraud': 0,
    'burglulary': 0,
    'trespass': 0,
    'assault': 0,
    'vandalism': 0,
    'disorderly conduct': 0,
    'motor vehicle theft': 0,
    'drugs': 0,
    'arson': 0,
    'liquor laws': 0,
    'robbery': 0,
    'aggravated assault': 0,
    'duii': 0,
    'forgery': 0,
    'runaway': 0,
    'curfew': 0,
    'stolen property': 0,
    'sex offenses': 0,
    'weapons': 0,
    'kidnap': 0,
    'embezzlement': 0
    }
    for dict_ in range(len(data)):
        crime_count['total_crimes'] += 1
        if dict_['major_offense_type'] == 'larceny':
            crime_count['larceny'] += 1
            # do this for every crime in the dict dumb bitch


# crime_count = {
#     amnt_larceny = crime_count['larceny'],
#     amnt_fraud = crime_count['fraud'],
#     amnt_burgulary = crime_count['burgulary'],
#     amnt_trespass = crime_count['trespass'],
#     amnt_assault = crime_count['assault'],
#     amnt_vandalism = crime_count['vandalism'],
#     amnt_disorderly_conduct = crime_count['disorderly conduct'],
#     amnt_mvt = crime_count['motor vehicle theft'],
#     amnt_drugs = crime_count['drugs'],
#     amnt_arson = crime_count['arson'],
#     amnt_liquor_laws = crime_count['liquor laws'],
#     amnt_robbery = crime_count['robbery'],
#     amnt_aggravated_assault = crime_count['aggravated assault'],
#     amnt_duii = crime_count['duii'],
#     amnt_forgery = crime_count['forgery'],
#     amnt_runaway = crime_count['runaway'],
#     amnt_curfew = crime_count['curfew'],
#     amnt_stolen_property = crime_count['stolen property'],
#     amnt_sex_offenses = crime_count['sex offenses'],
#     amnt_weapons = crime_count['weapons'],
#     amnt_kidnap = crime_count['kidnap'],
#     amnt_embezzlement = crime_count['embezzlement']
# }





# def crime_type_list():
# type = []
# for y in range()


# def crime_year_list():
#     yr = []


 

# def common_crimes():
#     pass



# def year_counter():
#     pass