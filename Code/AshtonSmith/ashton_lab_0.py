#This file serves as a graveyard for my larger pieces of deleted code
        #Lab12
        # if radSelected == 1:
        #     temp = str(self.atm.check_balance())
        #     self.label4.configure(text = 'Current blance = ' + temp)
        # elif radSelected == 2:
        #     #temp = str(self.atm.withdraw())v
        #     self.label4.configure(text = temp + '$ withdrawn')
        # elif radSelected == 3:
        #     #self.atm.deposit()
        #     self.label4.configure(text = temp + '$ deposited')
        # elif radSelected == 4:
            #temp = self.atm.calc_interest()
            #self.atm.deposit(temp)
            # temp = str(temp)
            # self.label4.configure(text = temp + '$ interest earned')

        #self.label.grid(column = 50, row = 20)


    # main.destroy()
    # main=Frame(root)
    # Or in a button:

    # def clear():
    #     global main, root
    #     main.destroy()
    #     main=Frame(root)
    #     main.pack()
    # clearbtn=Button(main, text='clear', command=clear)
    # clearbtn.pack()
    # To clear the screen. You can also just create a new window the same way as you created root(not recommended) or create a toplevel instance, which is better for creating multiple but essentially the same. You can also use grid_forget():

    # w=Label(root, text='whatever')
    # w.grid(options)



    # ws = Tk()
    # ws.title('get text demo')
    # ws.geometry('200x200')

    # def welcomeMessage():
    #     name = name_Tf.get()
    #     return messagebox.showinfo('message',f'Hi! {name}, Welcome to python guides.')
        

    # Label(ws, text="Enter Name").pack()
    # name_Tf.pack()

    # Button(ws, text="Click Here", command=welcomeMessage).pack()

            # self.label4.configure(text = name)
            #my_str = self.box


      #f.write('\n')
                #print(row)
            #     for j in self.contacts:#j = dict
            #         for z in range(len(j)):#z 
            #             f.write(z)
            #         f.write('\n')
            # # contacts = []
            # header = lines[0].split(',')
            # if header != self.header:
                # if len(self.contacts) > 0:
                    # return 'CSV not compatible'
            # for i in range(1, len(self.contacts)):
            #     row = lines[i].split(',')
            #     contact = dict(zip(header, row))
            #     contacts.append(contact)
            # self.contacts += contacts
            # self.header = header

#lab8
#this function doesnt work - the method attempted to fill valleys with water doesnt work for a list
#if the list was fed into a 2 dimensional array this method would work (after some debugging)
# def ground_printer(data):
#     highest = 0
#     water = 0
#     length = len(data)
#     for i in data:
#         if( i > highest):
#             highest = i
    
#     i = highest -1
#     while i > 0: # i = the height being drawn
#         x = 0 #current index
#         for j in data: #j = the current height of index
#             #print x
#             if j > i:
#                 print (' X ', end ='')
#             #print 0
#             #check left
#             #index not out of bounds and if there is an x to the left
#             elif ((i != 0) and j <= data[x - 1]):
#                 #check right
#                 #index not out of bounds and if there is an x to the right 
#                 if ((x + 1 < length) and (i + 1 < length) and (i + 1) > data[x + 1]):
#                     #check down
#                     if(i - 1 > 0) and (i  <= j+1):
#                         print(' 0 ', end = '')
#                     else:
#                         print('   ',end = '')
#             #print '  '
#             else: print('   ',end = '')

#             x += 1
#         print('')
#         i -=1


#lab03
#ALTERNATE FUNCTION VERSION
# thisversion of the function only prints and does not return the result
# #This function converts an integer from 0-999 to its english representation
# def number_converter(num):
#     num2 = str(num) #used to store the number as a string, so it can be indexed
#     length = len(num2)
    
#     if(length == 1):
#         num2 = int(num2)
#         print(ones_dict[num])
#     elif (length == 2):
#         if num <= 19:
#             print(ones_dict[num])
#         else:
#             if(num2[1] == '0'):
#                 print(tens_dict[int(num2[0])])
#             else:
#                 print(tens_dict[int(num2[0])] + ones_dict[int(num2[1])])
#     elif (length == 3):
#         print(ones_dict[int(num2[0])] + ' hundred ', end = '')
#         num3 = num2[1] + num2[2]
#         num3 = int(num3)
#         if num3 <= 19:
#             print(ones_dict[num3])
#         else:
#             if(num2[2] == '0'):
#                 print(tens_dict[int(num2[1])])
#             else:
#                 print(tens_dict[int(num2[1])] + ''+ ones_dict[int(num2[2])])

#lab3 
#this function was replaced with a function that returns the string instead of printing it inside the function
# #this function converts the argument to a roman numeral
# def roman_converter(num):
#     num2 = str(num) #used to store the number as a string, so it can be indexed
#     length = len(num2)
#     #1 digit 
#     if(length == 1):
#         num2 = int(num2)
#         print(roman_ones_dict[int(num)])
#     #2 digits
#     elif (length == 2):
#         if(num2[1] == '0'):
#             print(roman_tens_dict[int(num2[0])])
#         else:
#             print(roman_tens_dict[int(num2[0])] + roman_ones_dict[int(num2[1])])
#     #3 digits
#     elif (length == 3):
#         if(num2[1] == '0' and num2[2] == '0'):
#             print(roman_hundreds_dict[int(num2[0])])
#         elif(num2[1] == '0'):
#             print(roman_hundreds_dict[int(num2[0])] + roman_ones_dict[int(num2[2])])
#         elif(num2[2] == '0'):
#             print(roman_hundreds_dict[int(num2[0])] + roman_tens_dict[int(num2[1])])
#         else: 
#             print(roman_hundreds_dict[int(num2[0])] + roman_tens_dict[int(num2[1])] + roman_ones_dict[int(num2[2])])

