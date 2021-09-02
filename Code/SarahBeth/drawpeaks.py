data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]


# for i in range(len(data)):
# def find_peaks(data):
#     peaks = []
#     iterate through data
#         if data[i] is greater than data[i-1] and greater than data[i+1]:
#             peaks.append[data[i]]

# def find_valley(data):
#     valleys = []
#     iterate through data
#         if data[i] is less than data[i-1] and less than data[i+1]:
#             valleys.append[data[i]]

def draw_peaks_valleys(data):
    rows = max(data) #aren't going to exceed heighest data point 
    cols = len(data)
    for i in range(rows, 0, -1): # iterate over the rows
        for j in range(cols): # iterate over the columns
            if data[j] >= i:
                print('X', end=' ')
            else:
                print(' ', end=' ')
        print() # after drawing the row, go to the next line

draw_peaks_valleys(data)