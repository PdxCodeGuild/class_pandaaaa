from pairmaker import Student

Hello = Student('theo', {})

print(Hello)
# def parse_data():
#     with open('mt_tabor_rain.txt', "r") as rain_data_string:
#         line = rain_data_string.readlines()
#         # print(line)
#         #parse date and total rain fall
#         for n in range(11, len(line)):
#             line_string = line[n]
#             rain_count = line_string[14:17].replace(" ", "")
#             print(rain_count)
#             if rain_count[0] in string.digits:
#                 rain_count = int(rain_count)
#                 dict_rain_data[line_string[0:11]] = rain_count #parse date and total rain fall into a dictionary

# parse_data()
# def get_contacts():
#   with open('mt_tabor_rain.txt', "r") as f:
#     lines = f.readlines()
#     headers = lines.pop(0).strip().split(',')

#     contacts = []

#     for line in lines:
#       columns = line.strip().split(',')
#     print(columns)

# get_contacts()