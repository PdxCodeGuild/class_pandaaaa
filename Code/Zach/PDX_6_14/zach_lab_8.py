#Zach Watts
#Lab 8: Peaks and Valleys

def main():
    data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
    peaks(data)
    valleys(data)
    peaks_and_valleys(data)
    exit()

def peaks(data):
    peaks = []
    for i in range(1, len(data) - 1):
        if data[i-1] < data[i] and data[i] > data[i+1]:
                peaks.append(data[i])
    return peaks


def valleys(data):
    valleys = []
    for i in range(1, len(data) - 1):
        if data[i-1] > data[i] and data[i] < data[i+1]:
                valleys.append(data[i])
    return valleys

def peaks_and_valleys(data):
    ps_and_vs = []
    for i in range(1, len(data) - 1):
        if data[i-1] > data[i] and data[i] < data[i+1]:
            ps_and_vs.append(data[i])
        elif data[i-1] < data[i] and data[i] > data[i+1]:
            ps_and_vs.append(data[i])
    print(ps_and_vs)
    return ps_and_vs

def graph(data):
    graph_ = []
    for num in data:
        graph_.append('X'*num)
    exit()

main()