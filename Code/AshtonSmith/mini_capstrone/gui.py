from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import requests
import os
from dotenv import load_dotenv
from requests.api import delete
import spoon_api

class Window(Tk):
    def __init__(self):
        super(Window, self).__init__()
        # root = tk.Tk()
        self.current = 0 
        self.title("Recipe Finder")
        self.minsize(500,400)
        self.ingredients = ''
        self.label_search = tk.Label(self, text = 'Enter a search term: ')
        self.label_search.pack()
        self.box_search = tk.Text(width= 10, height= 1)
        self.box_search.pack()
        self.button_search = tk.Button(self, text = 'search', command = self.click_search)
        self.button_search.pack()
    
    
    #clears window with destroy()
    def screen_clear(self):
        self.img_label.destroy()
        self.label_steps.destroy()
        self.label_ingredients.destroy()
        self.button_next.destroy()

    def next_button(self):
        self.screen_clear()

        return 0

    def click_search(self):
        name = StringVar(self)
        name = self.box_search.get('1.0', 'end-1c')
        self.label_search.destroy()
        self.box_search.destroy()
        self.button_search.destroy()
        cat = spoon_api.category(1)
        my_spoon = spoon_api.spoon(cat, name)
        self.data_printer(my_spoon.get_data())
        self.pack_img(self.curr_image)
        self.label_ingredients = tk.Label(self, text = self.ingredients)
        self.label_ingredients.pack()
        self.label_steps = tk.Label(self, text = self.my_steps)
        self.label_steps.pack()
        self.button_next = tk.Button(self, text = 'Next', command = self.next_button)
        self.button_next.pack()

    def data_printer(self,my_data):
            if 'code' in my_data and my_data['code'] == 401: #401 unauthorized
                print('error 401')
                return 0

            print('Matches found: ' + str(my_data['totalResults']))
            
            #loop through results (list of recipes)    
            for i in my_data['results']:
                self.curr_image = i['image']
                curr_id = i['id'] #recipe id

                #request full recipe using id
                load_dotenv()
                TOKEN = os.getenv('TOKEN') #api key
                cur_url = f'https://api.spoonacular.com/recipes/{curr_id}/information?includeNutrition=true&apiKey={TOKEN}'
                response = requests.get(cur_url)
                data = response.json()
                
                self.my_title = data['title']
                #print ingredients
                for i in data['extendedIngredients']:
                    self.ingredients += i['originalString'] + '\n'
            
                #print instructions
                self.my_steps = ''
                for i in data['analyzedInstructions']:
                    for j in i['steps']:
                        self.my_steps += 'Step ' + str(j['number']) +': ' + str(j['step']) +'\n\n'
                
                break 
               


    # def populate_window(self, spoon_dat):    
    #     self.label = tk.Label(self, text = 'TITLE')
    #     self.label.pack()
       
    #     self.button = tk.Button(self, text = 'Next', command = self.click_me())
    #     self.button.pack()


    #     self.label2 = tk.Label(self, text = spoon_dat)
    #     self.label2.pack()

      
    def pack_img(self, img_name):   
        img = Image.open(requests.get(img_name, stream= True).raw)#open image associated with result
        # img = Image.open(img_name)
        img = img.resize((250, 250))
        tkimage = ImageTk.PhotoImage(img)
        self.img_label = tk.Label(self, image=tkimage)
        self.img_label.image = tkimage
        self.img_label.pack()
 # gui.window.pack_img(curr_image)
# image = Image.open(requests.get(curr_image, stream= True).raw)#open image associated with result
# image.show()

    # def click_me(self):
    #     return 0



def main():
   
    # query = spoon_api.prompt_query()
    # query = 'ye'
    # my_spoon = spoon_api.spoon(cat, query)
    # spoon_dat = my_spoon.get_data()


    window = Window()
    window.mainloop()

main()