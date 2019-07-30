import random

students = ['Ana', 'Eva', 'Svanhvit', 'Wendy', 'Edgar', 'Marcos']

random.shuffle(students)

group1 = students[0:1]
group2 = students[1:2]

combined = zip(group1, group2)

for first_student, second_student in combined:
    print(first_student, " and" second_student)
