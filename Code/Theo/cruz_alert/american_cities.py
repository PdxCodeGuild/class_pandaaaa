import json
from pprint import pprint

class Cities:
    def __init__(self,input_file='cities.json'):
        self.input_file = input_file
        self.city_list = []
        self.total_cities = 0
        
    def __str__(self):
        output = ''
        for i in range(self.total_cities):
            output += self.city_list[i].name + ', '
            output += self.city_list[i].state
            output += '\n'
        return output
    
    def read_file(self):
        with open (self.input_file) as f:
            text = f.read()
        data =  json.loads(text)
        self.total_cities = len(data)
        print(self.total_cities)
        for i in range(self.total_cities):
            new_city = City(data[i])
            self.city_list.append(new_city)

class City:
    def __init__(self,city_data):
        self.name = city_data['city']
        self.latitude = city_data['latitude']
        self.longitude = city_data['longitude']
        self.state = city_data['state']
        
    def __str__(self):
        return f'{self.name}'    
def main():
    cities = Cities()
    cities.read_file()
    print(cities)
    exit()

def load():
    return Cities()

    
    
if __name__ == "__main__":
    main()