from django.shortcuts import render, get_object_or_404, redirect
from .pylabs import ari_lab, rot_lab, numphrase_lab, unit_lab
from random import randint

# Create your views here.



def home(request):
    return render(request, 'masterlab\labs\home.html')


def display_ari(request,ari_text):
    # ari_text = 'temp'
    context = {
        'ari_score':ari_lab.manage(ari_text),
    }
    return render(request, 'masterlab\labs\display_ari.html', context)

def ari(request):
    # ari_text = get_object_or_404(ari_model)
    if request.method == 'POST':
        ari_text = request.POST.get('ari_text')
        # return redirect('display_ari')
        return display_ari(request, ari_text)
    else:
        ari_text = 'x'
    context = {
        'ari_score':ari_lab.manage(ari_text),
    }
    print(ari_text)
    print(context['ari_score'])
    return render(request, 'masterlab\labs\labari.html', context)


def rps(request):
    if request.method == 'POST':
        choice = request.POST.get('choice')
        return display_rps(request,choice)
    return render(request, 'masterlab\labs\labrps.html')

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

def rot(request):
    if request.method == 'POST':
        my_str = request.POST.get('rot_text')
        return display_rot(request,my_str)
    return render(request, 'masterlab\labs\labrot.html')


def display_rot(request, my_str):
    result = rot_lab.convert_to_rot(my_str)
    result_converted = rot_lab.convert_from_rot(result)
    context = {
        'result':result,
        'converted_back':result_converted,
    }
    return render(request, 'masterlab\labs\display_rot.html', context)

def nump(request):
    if request.method == 'POST':
        my_num = request.POST.get('num_text')
        option = request.POST.get('radio_choice')
        return display_nump(request,my_num,option)
    return render(request, 'masterlab\labs\labnump.html')

def display_nump(request, my_num, option):
    if option == '1':
        result = numphrase_lab.number_converter(my_num)
    else:
        result = numphrase_lab.roman_converter(my_num)

    context = {
        'my_num':my_num,
        'result':result,
    }
    return render(request, 'masterlab\labs\display_nump.html',context)

def unit(request):
    if request.method == 'POST':
        unit_1 = request.POST.get('unit_1')
        unit_2 = request.POST.get('unit_2')
        my_num = request.POST.get('my_num')
        return display_unit(request, unit_1, unit_2, my_num)
    return render(request, 'masterlab\labs\labunit.html')


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
