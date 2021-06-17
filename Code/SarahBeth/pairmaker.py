# pair maker 

import random 
from itertools import combinations


students = ['Theo', 'Zach', 'Brea', 'Ashton']

def random_pairs(students):
    #method 1
    pair1 = [students[i] for i in random.sample(range(len(students)), 2)] 
    # pair2 = [students[i] for i in random.sample(range(len(students)), 2) if students[i] not in pair1]
    pair2 = []
    for student in students: 
        if student not in pair1:
            pair2.append(student)
    print(f'pair 1:{pair1} pair2:{pair2}')


    # for comb in combinations(students, 2):
    #     print(comb)

def mob_typer(students):
    typer = random.choice(students)
    print(f'{typer} you have been CHOSEN')


random_pairs(students)
# mob_typer(students)