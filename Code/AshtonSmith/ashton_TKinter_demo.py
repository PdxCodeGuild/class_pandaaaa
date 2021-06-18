from tkinter import *
from tkinter import ttk

class Window(Tk):
    def __init__(self):
        super(Window, self).__init__()

        self.title("My Label")
        self.minsize(500,400)
        #self.wm_iconbitmap("myicon.ico")
        # self.createLabel()
        #self.create_layout()
        
        self.label = ttk.Label(self, text = 'application')
        self.label.grid(column = 1, row = 0)


        self.button = ttk.Button(self, text = 'Click me', command = self.click_me)
        self.button.grid(column = 0, row = 0)

    def click_me(self):
        self.label.configure(text = 'text is changed')
        self.label.configure(foreground = 'red', background = 'yellow')
        self.button.configure(text = 'button changed')

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