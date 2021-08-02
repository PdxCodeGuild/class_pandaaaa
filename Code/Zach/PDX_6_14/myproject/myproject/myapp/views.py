from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import NumForm

word_dict = {
0 : ["zero"],
1 : ["one", "", "one-hundred"],
2 : ["two", "twenty", "two-hundred"],
3 : ["three", "thirty", "three-hundred"],
4 : ["four", "fourty", "four-hundred"],
5 : ["five", "fifty", "five-hundred"],
6 : ["six", "sixty", "six-hundred"],
7 : ["seven", "seventy", "seven-hundred"],
8 : ["eight", "eighty", "eight-hundred"],
9 : ["nine", "ninety", "nine-hundred"],
10 : "ten",
11 : "eleven",
12 : "twelve",
13 : "thirteen",
14 : "fourteen",
15 : "fifteen",
16 : "sixteen",
17 : "seventeen",
18 : "eighteen",
19 : "nineteen"
}

def myview(request):
    
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NumForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            num = form.cleaned_data.get('numbers')
            words = one_hundred_to_999(num)
            print(words)
            return HttpResponse(words)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NumForm()

    return render(request, 'myapp/mytemplate.html', {'form': form})

def number():
    valid = 0
    while not valid:
        try:
            num = int(input("Enter an integer between 0 and 999:  "))
            #if num < 0 or num > 99:
                #print('Integer must be between 0 and 999!')
                #continue
            valid = 1
        except(ValueError):
            print("Input must be an integer")
            break
    return num


def zero_to_99(num):
    tens_dig = num//10
    ones_dig = num % 10
    if tens_dig == 0 and ones_dig == 0:
        return ""
    elif num < 10:
        return word_dict[num][0]
    elif 9 < num < 20:
        return word_dict[num]
    elif num >= 20:
        #print(tens_dig)
        if ones_dig == 0:
            return word_dict[tens_dig][1]
        elif tens_dig == 0:
            return f'{0}{word_dict[ones_dig][0]}'
        elif ones_dig > 0:
            return f'{word_dict[tens_dig][1]}-{word_dict[ones_dig][0]}'

def one_hundred_to_999(num):
    if num < 100:
        return zero_to_99(num)
    elif num >= 100:
        hundred = num//100
        ten_and_ones = num%100
        return f'{word_dict[hundred][2]} {zero_to_99(ten_and_ones)}'
#add one with this: /num2phrase/

from django.shortcuts import render
from django.http import HttpResponse
from .models import MyModel

# def myview(request):
#     myinstances = MyModel.objects.all()
#     context = {
#         'myinstances': myinstances
#     }
#     return render(request, 'myapp/mytemplate.html', context)

def mycreate(request):
    print(request.POST)
    return HttpResponse('form received')