# Lab 8: Peaks and Valleys

def main():
    ground_list = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9, 10, 9 ,8, 7, 6, 7, 8, 9, 10]
    ground_printer(ground_list)   
    water_ground_printer(ground_list)
    input("done?")
    return 0



#this function returns peaks(high points) as a list
def peaks(data):
    current_high = 0
    current_location = 0
    my_peaks = []
    for i in data:
        if(i > current_high):
            current_high = i
        elif(i < current_high):
            if(data[current_location-1] == current_high):
                my_peaks.append(current_location-1)
        current_location += 1
    return(my_peaks)



#this function returns valleys(low points) as a list
def valleys(data):
    my_len = len(data)
    current_location = 0
    my_valleys = []
    for i in data:
        if(current_location != 0 and current_location+1 < my_len):
            if((data[current_location-1] == data[current_location+1]) and (data[current_location -1] > data[current_location])):
                my_valleys.append(current_location)
        current_location += 1
    return my_valleys



#this function returns all peaks and valleys as a list
def peaks_and_valleys(data):
    my_pv = []
    temp = []
    temp += (peaks(data))
    temp += (valleys(data))
    remaining  = len(temp)
    while(remaining):
        high = 0
        index = 0
        for i in temp:
            if high < i:
                my_pv.append(temp.pop(index))
            else:
                high = i
            index +=1
        remaining -= 1
    return my_pv               



#this function prints the ground, but also fills between peaks with water(0s)
def water_ground_printer(data):
    my_peaks = peaks(data)
    my_valleys = valleys(data)

    peak_found = False
    highest = 0
    water_low = 0
    water_high = 0
    cur_valley = 0
    for i in data:
        if( i > highest):
            highest = i
    i = highest
    x = 0
    while i > 0: # i = current height (y) (starting from top)
        for j in data: #x = current index (x)
            if j > i:
                print (' X ', end ='')
                if(my_peaks and x == my_peaks[-1]):
                    water_high = my_peaks.pop(-1)
                    curr_peak = x
                if(my_valleys and x == my_valleys[-1]):
                    water_low = my_valleys.pop(-1)
                    curr_valley = x
            elif (i <= water_high) and (x > curr_peak) and (i >= cur_valley):
                print(' 0 ', end = '')
            else: 
                print('   ',end = '')
            x += 1
        print('')
        i -= 1
        x = 0
        


#this function prints the ground
def ground_printer(data):
    highest = 0
    water = 0
    for i in data:
        if( i > highest):
            highest = i
    i = highest
    while i > 0:
        for j in data:
            if j > i:
                print (' X ', end ='')
            else: print('   ',end = '')
        print('')
        i -=1
