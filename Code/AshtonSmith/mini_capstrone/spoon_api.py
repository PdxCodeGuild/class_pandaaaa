#external
import requests
import os
from dotenv import load_dotenv
from PIL import Image


#this function is used to prompt the user for the category to search for. 
# It is returned as a string (cooresponding cat_dict key)
def prompt_category():
    cat_dict = {
    1:'recipes',
    2:'ingredients',
    3:'menuItems',
    4:'products'
    }
    print('\nWhat category would you like to search?')
    option = 0
    again = True
    while again:
        print(
        '''
        1. Recipes\n
        2. Ingredients\n
        3. Menu items\n
        4. Products
        ''')
        try:
            option = input()
            option = int(option)
            again = False
        except ValueError:
            pass
        if option != 1 and option != 2 and option != 3 and option != 4:
            print('invalid option')
    return cat_dict[option] 



#this class is used to prompt the user for what they want to search for (query)
def prompt_query():
    return input("What do you want to search for?\n")



#this class is used to make requests to spoon api
class spoon_api:
    def __init__(self,category,query) -> None:
        self.category = category
        self.query = query
        pass


    #this function is used to make a request to spoon
    def get_data(self):
        url_dict = {
            'recipes' : 'recipes/complexSearch?',
            'ingredients':'food/ingredients/search?',
            'menuItems': 'food/menuItems/search?',
            'products': 'food/products/search?'
        }
        load_dotenv()
        TOKEN = os.getenv('TOKEN')
        url = f'https://api.spoonacular.com/{url_dict[self.category]}query={self.query}&apiKey={TOKEN}'

        # url = f'https://api.spoonacular.com/{url_dict[self.category]}query={self.queryu&=true&apiKey={TOKEN}'

        response = requests.get(url)
        data = response.json()
        # print(data)
        return data



# my_spoon.get_data()
cat = prompt_category()
query = prompt_query()

my_spoon = spoon_api(cat, query)
my_data = my_spoon.get_data()


for i in my_data['results']:
    curr_image = i['image']
    image = Image.open(requests.get(curr_image, stream= True).raw)
    image.show()
    curr_id = i['id']
# https://api.spoonacular.com/recipes/{id}/information
    load_dotenv()
    TOKEN = os.getenv('TOKEN')
    # cur_url = f'https://api.spoonacular.com/recipes/{curr_id}'
    cur_url = f'https://api.spoonacular.com/recipes/{curr_id}/information?includeNutrition=false&apiKey={TOKEN}'
    response = requests.get(cur_url)
    data = response.json()
    for i in data['extendedIngredients']:
        print(i['name'])
        print(i['image'])
    
    # for i in data['']
    for i in data['analyzedInstructions']:
        for j in i['steps']:
            # print('Ingredients required in this step:')
            # for k in j['ingredients']:
            #     print(k['localizedName'])
            print ('\nStep ' + str(j['number']) + ': ')
            print (j['step'] + '\n')
    if input('Enter x to exit') == 'x':
        break

















# https://api.spoonacular.com/recipes/716429/information?includenutrition=false

# im = Image.open(requests.get(url, stream=True).raw)
    # # https://api.spoonacular.com/recipes/findByIngredients?ingredients=apples,+flour,+sugar&number=2
    # url = f'https://api.spoonacular.com/recipes/findByIngredients?ingredients=apples,+flour,+sugar&number=2?apikey={token}'
    # # url = f'https://favqs.com/api/quotes?page=1&filter={term}'
    # # last_page = False
    # # again = ''
    # # payload ={ 
    # #     'page' : '1',
    # #     'term' : f'{term}'
    # # }
    # load_dotenv()
    
    # # headers = {'Authorization': 'Token token="' + str(token) + '"'}