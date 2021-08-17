from tkinter import *
from tkinter import ttk

COLOR1 = 'Red'
COLOR2 = 'Blue'
COLOR3 = 'Yellow'
class Window(Tk):
    def __init__(self):
        super(Window, self).__init__()

        self.title("My Label")
        self.minsize(500,400)
        # self.label = ttk.Label(self, text = 'application')
        # self.label.grid(column = 1, row = 0)
        self.create_combo()
        self.create_radio()
    def rad_event(self):
        radSelected = self.radValues.get()
        if radSelected == 1:
            self.configure(background=COLOR1)
        elif radSelected == 2:
            self.configure(background=COLOR2)
        elif radSelected == 3:
            self.configure(background=COLOR3)
       

    def create_radio(self):
        self.radValues = IntVar()
        self.rad1 = ttk.Radiobutton(self,text = COLOR1, value = 1, variable = self.radValues , command = self.rad_event)
        self.rad1.grid(column = 5, row = 5, sticky = W, columnspan = 3)

        self.rad2 = ttk.Radiobutton(self,text = COLOR2, value = 2, variable = self.radValues , command = self.rad_event)
        self.rad2.grid(column = 6, row = 6, sticky = W, columnspan = 3)

        self.rad3 = ttk.Radiobutton(self,text = COLOR3, value = 3, variable = self.radValues , command = self.rad_event)
        self.rad3.grid(column = 7, row = 7, sticky = W, columnspan = 3)


    def create_combo(self):
        self.languages = StringVar()
        self.combobox = ttk.Combobox(self, width = 20, textvariable = self.languages)
        self.combobox['values'] = ('python', 'java', 'C++', 'C#', 'Ruby', 'Php', 'CSS')
        
        self.combobox.grid(column = 0, row = 1)

        self.label = ttk.Label(self, text = 'Select your language')
        self.label.grid(column = 0, row = 0)

        self.button = ttk.Button(self, text = 'click me', command = self.click_me)
        self.button.grid(column = 2, row =0)

    def click_me(self):
        self.label.configure(text ='selected : ' + self.languages.get())

















# ##############
#         self.text_entry()
    

#     def click_me(self):
#         self.label.configure(text = 'Hello ' + self.name.get())
#     def text_entry(self):
#         self.name = StringVar()
#         self.label == ttk.Label(self, text ='enter your name')
#         self.label.grid(column = 15, row = 0)

#         self.textbox = ttk.Entry(self, width = 20,  textvariable = self.name)
#         self.textbox.focus()
#         self.textbox.grid(column = 15, row = 1)

#         self.button = ttk.Button(self, text = 'click me', command = self.click_me)
#         self.button.grid(column = 15, row = 2)





#####################
        #self.wm_iconbitmap("myicon.ico")
        # self.createLabel()
        #self.create_layout()
       ################ 
        


        #  self.button = ttk.Button(self, text = 'Click me', command = self.click_me)
        #  self.button.grid(column = 0, row = 0)

    # def click_me(self):
    #     self.label.configure(text = 'text is changed')
    #     self.label.configure(foreground = 'red', background = 'yellow')
    #     self.button.configure(text = 'button changed')
##############
    # def createLabel(self):
    #     labelFont = ('times', 40 , 'bold')
    #     label = Label(self, text = "TKinter Label Creation")
    #     label.config(font = labelFont, bg ='black', fg ='blue')
    #     label.grid(column = 0, row = 0)

    # def create_layout(self):
    #     Label(self, text = "Pack layout example").pack()
    #     Button(self, text = 'button ').pack()
    #     Button(self, text = 'expand = 1').pack(expand = 1)
    #     Button(self, text = 'fill = x, expand = 1').pack(fill = X, expand = 1)

    #     Button(self, text = 'LEFT').pack(side = LEFT)
    #     Button(self, text = 'BOTTOM').pack(side = BOTTOM)
    #     Button(self, text = 'RIGHT').pack(side = RIGHT)


window = Window()
window.mainloop()