filename ='..\..\Data\phonebook.txt'
try:
    f = open(filename)
    #print(type(f))
    contents = f.read()
    print(contents)
    f.close()
except(IOError):
    print(f"Could not open {filename}")