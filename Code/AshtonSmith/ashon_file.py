#import os
#DOES work
#f = open('C:/Users/ashto/pdx_code/Panda/class_pandaaaa/Code/AshtonSmith/ashton_lab_0.py', 'r')
#f = open('Code/AshtonSmith/ashton_lab_0.py', 'r')

#DOESNT work
#f = open('ashton_lab_0.py', 'r')
#f = open('ashtonsmith/ashton_lab_0.py', 'r')
#f = open('AshtonSmith/ashton_lab_0.py', 'r')

#folder_path = '...'
contents = f.read()
print(contents)
f.close()