from django.shortcuts import render, get_object_or_404, redirect
from .pylabs import ari_lab, rot_lab, numphrase_lab, unit_lab
from random import randint


#home screen, serves as a navigaiton view
def home(request):
    return render(request, 'masterlab\labs\home.html')



#this view is used to take input for the ari calculator lab
def ari(request):
    if request.method == 'POST':
        ari_text = request.POST.get('ari_text')
        return display_ari(request, ari_text)
    else:
        ari_text = 'x'
    context = {
        'ari_score':ari_lab.manage(ari_text),
    }
    print(ari_text)
    print(context['ari_score'])
    return render(request, 'masterlab\labs\labari.html', context)


#this view is used to display an ari score
def display_ari(request,ari_text):
    context = {
        'ari_score':ari_lab.manage(ari_text),
    }
    return render(request, 'masterlab\labs\display_ari.html', context)



#this view is used to take user input for rock paper scissors.
def rps(request):
    if request.method == 'POST':
        choice = request.POST.get('choice')
        return display_rps(request,choice)
    return render(request, 'masterlab\labs\labrps.html')



#this view is used to decide a random choice for the computers move,
#then display the results of rock paper scissors.
def display_rps(request, choice):
    context = { 'choice':choice}
    print(choice)
    choice_dict = {
        1:'rock',
        2:'scissors',
        3:'paper',
    }
    context = { 
        'user_choice':choice,
        'cpu_choice':choice_dict[randint(1,3)],
        }
    return render(request, 'masterlab\labs\display_labrps.html', context)



#this view is used to take a text input to convert to rot13.
def rot(request):
    if request.method == 'POST':
        my_str = request.POST.get('rot_text')
        return display_rot(request,my_str)
    return render(request, 'masterlab\labs\labrot.html')



#this view is used to display a converted string to rot 13, 
#and also displays it converted back.
def display_rot(request, my_str):
    result = rot_lab.convert_to_rot(my_str)
    result_converted = rot_lab.convert_from_rot(result)
    context = {
        'result':result,
        'converted_back':result_converted,
    }
    return render(request, 'masterlab\labs\display_rot.html', context)



#this view is used for the number printer lab.
#The user enters a text and the choice to display as text or roman numeral.
def nump(request):
    if request.method == 'POST':
        my_num = request.POST.get('num_text')
        option = request.POST.get('radio_choice')
        return display_nump(request,my_num,option)
    return render(request, 'masterlab\labs\labnump.html')



#this view is used to display the nump lab results.
def display_nump(request, my_num, option):
    if option == '1':
        result = numphrase_lab.number_converter(int(my_num))
    else:
        result = numphrase_lab.roman_converter(int(my_num))
    context = {
        'my_num':my_num,
        'result':result,
    }
    return render(request, 'masterlab\labs\display_nump.html',context)



#this view is used to get data for the unit conversion lab. 
def unit(request):
    if request.method == 'POST':
        unit_1 = request.POST.get('unit_1')
        unit_2 = request.POST.get('unit_2')
        my_num = request.POST.get('my_num')
        return display_unit(request, unit_1, unit_2, my_num)
    return render(request, 'masterlab\labs\labunit.html')



#this view is used to display the conversion done by the unit conversion lab.
def display_unit(request, unit_1, unit_2, my_num):
    result  = unit_lab.manager(unit_1, unit_2, float(my_num))
    context = {
        'my_num':my_num,
        'unit_1':unit_1,
        'unit_2':unit_2,
        'result':result
    }
    print(context)
    return render(request, 'masterlab\labs\display_unit.html',context)