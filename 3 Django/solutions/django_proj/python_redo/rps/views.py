from django.shortcuts import render
import random

def calc_winner(user_choice, pc_choice):
	defeats = {'rock': 'scissors',
			   'paper': 'rock',
			   'scissors': 'paper'}
	if user_choice == pc_choice:
		return 'tie!'
	elif defeats[user_choice] == pc_choice:
		return 'win!'
	else:
		return 'lose!'

def index(request): 
  if request.method == 'POST':
    choices = ['rock', 'paper','scissors']
    user_choice = request.POST['choice']
    computer_choice = random.choice(choices)
    result = calc_winner(user_choice, computer_choice)
    context = {
        'played': True,
        'winner': result,
        'computer_choice': computer_choice,
        'user_choice': user_choice,
    }
    return render(request, 'rps.html', context)
  else:
    context = {
        'played': False,
        'winner': 'no winner yet',
        'user_choice': 'you havent chosen',
    }      
    return render(request, 'rps.html', context)


