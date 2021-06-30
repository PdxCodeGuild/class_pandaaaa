#Lab 2, now with args!
import average_num as avg
def main():
    nums = []
    while True:
        val = avg.add_num()
        if val.lower() == 'done':
            print(round(avrg(*nums),2))
            break
        else:
            try:
                nums.append(int(val))
            except(ValueError):
                print(f"{val} isn't an integer. Try again.")
    exit()

def avrg(*args):
    sum = 0
    count=0
    for arg in args:
        sum += arg
        count += 1
    return sum / count

main()