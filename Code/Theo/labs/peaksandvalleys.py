def main():
    data = [1 , 2 , 3 ,4 , 5 , 6 , 7 , 6 , 5 , 4 , 5 , 6 , 7 , 8 , 9 , 8 , 7 , 6 , 7 , 8 , 9]
    peak_indices = peaks(data)
    valley_indices = valleys(data)
    print(valley_indices)
    print(peak_indices)
    print(peaks_and_valleys(peak_indices,valley_indices))
    visualization(data)
    exit()


def peaks(data):
    peak_indices = []
    i = 1
    n = len(data)
    while i < n-1:
        if data[i-1] < data[i] and data[i+1] < data[i]:
            peak_indices.append(i)
        i += 1
    return peak_indices

def valleys(data): 
    valley_indices = []
    i = 1
    n = len(data)
    while i < n-1:
        if data[i-1] > data[i] and data[i+1] > data[i]:
            valley_indices.append(i)
        i += 1
    return valley_indices

def peaks_and_valleys(peaks,valleys):
    p_v = []
    p_v.extend(peaks)
    p_v.extend(valleys)
    p_v.sort()
    return p_v

def visualization(data):
    line = []
    i = 0
    j = 0
    max = 0
    for val in data:
        if val > max:
            max = val
            
    n = len(data)
    for i in range(max):
        for j in range(n):
            if data[j] >= max-i:
                line.append('X')
            else:
                line.append(' ')
        print(line)
        line.clear()
main()