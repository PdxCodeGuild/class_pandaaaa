from tkinter import *
from tkinter import messagebox 

def add_item(): # defining a funtion
    task = user_entry.get() # get data from user entry box and saves it to task variable
    if task != "": # checking to see if user entry box is not blank
        box.insert(END, task) # inserting the task at the end of the listbox
        # the first parameter in the inset function determines the location, the second parameter is what is to be entered, can be index position number
        user_entry.delete(0, "end") # clearing the user entry box
    else:
        messagebox.showwarning('Error', 'Please enter a task') # creating a pop up message box, first index defines name of the window in the pop up error message
 # showwarning is a function of the messagebox class


def delete_item(): 
    box.delete(ANCHOR)   # delete is a built in function, anchor refers to selected item

##### defining window specs
window = Tk() # class to initiate screen from tkinter
window.geometry("500x450+500+200")  # defining task window
window.title("Brea's Chore List") # declaring a title
# window.config(bg='#a57bfe') # background color
window.resizable(width=False, height=False) # window is not resizable
#####

frame = Frame(window) # frame class creating a frame inside of parent window 
frame.pack(pady=10) 

box = Listbox(  # defining the task list box and its characteristics
    frame, 
    width=30, # width of the task box
    height=10, # height of the task box
    highlightthickness=0, #highlight property of listbox
    bd = 0,
    font=('times', 18), # font style and size
    # selectbackground='#a6a7a7', # 
    activestyle="none",
)

box.pack(side=LEFT, fill=BOTH) # places the box, fills entire space in box

agenda = []   # to do list items

for item in agenda: # for loop to add items
    box.insert(END, item) #inserts item at the end of box

scroller = Scrollbar(frame)  # class defining scrollbar in the frame
scroller.pack(side=RIGHT, fill=BOTH) # the scrollbar is in the right side of the frame

box.config(yscrollcommand=scroller.set) # config used to access an object's attributes after its initialisation
scroller.config(command=box.yview) 

user_entry = Entry( # built in class to add in user entries
    window,
    font=('times', 26) 
)

user_entry.pack(pady=20) # places the button

btn_frame = Frame(window) # placing button in a frame in the window
btn_frame.pack(pady=20) # set the padding of the y axis for the button frame


######## add button 
add_btn = Button( # built in class to make delete button
    btn_frame, # button frame
    font = 'times 16', # button font and font size
    text = 'Add Task', # add task button text
    command=add_item, # the function called when the button is clicked
    padx = 20, # size of horizontal part of button
    pady = 10, # size of vertical part of button
)
add_btn.pack(fill=BOTH, expand=True, side=LEFT) # places the button


######## delete button 
delete_btn = Button( # built in class to make delete button
    btn_frame, # button frame
    font = ('times 14'), # built in font
    text = 'Delete', # delete button text
    command=delete_item,# same as line 76
    padx = 20, # size of horizontal part of buttion
    pady = 10, # size of vertical part of button
)
delete_btn.pack(fill=BOTH, expand=True, side=RIGHT) # places the button


window.mainloop() # tk loop to keep loop open