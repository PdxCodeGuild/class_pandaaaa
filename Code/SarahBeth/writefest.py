def save_info():
    f = open(f'newfile.txt', 'w')
    f.write('hello again')
    f.close()

save_info()