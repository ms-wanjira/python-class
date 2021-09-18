marks = float(input("enter a number"))
y = marks
# if y <= 40 :
#     print('Grade E')
# elif y <= 49 :
#     print('Grade D')
# elif y <= 59:
#     print('Grade C')
# elif y <= 79:
#     print('Grade B')
# elif y > 79:
#     print('Grade A')
# else:
#     print('Did not do exams')

def grade(y):
    if y<=40:
        return 'Grade E'
    elif y<= 49:
        return 'Grade D'
    elif y <= 59:
        return 'Grade C'
    elif y <= 79:
        return 'Grade B'
    else:
        return'Grade A'

print(grade(y))