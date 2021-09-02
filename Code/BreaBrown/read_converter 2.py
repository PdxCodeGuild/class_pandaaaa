alpha_grade = ''
grade = int(input('Enter a grade 0-100: '))
if grade <= 100 and grade >= 90:
    alpha_grade = 'A'
elif grade <=89 and grade >= 80:
    alpha_grade = 'B'
elif grade <=79 and grade >= 70:
    alpha_grade = 'C'
elif grade <=69 and grade >= 60: 
    alpha_grade = 'D'
else:
    alpha_grade = 'F'    
print(f'Letter grade = {alpha_grade}')