#Задача №33. Решение в группах
#Хакер Василий получил доступ к классному журналу и
#хочет заменить все свои минимальные оценки на
#максимальные. Напишите программу, которая
#заменяет оценки Василия, но наоборот: все
#максимальные – на минимальные.
#Input: 5 -> 1 3 3 3 4
#Output: 1 3 3 3 1


def grade_fix(any_grade, quantity):
    if quantity == 0:
        return any_grade
    else:
        quantity -= 1
        if any_grade[quantity] > 3:
            any_grade[quantity] = 1
    return grade_fix(any_grade, quantity)  
    

grade = int(input("Какое количество оценок будем исправлять?"))
grade_list = []
for i in range(grade):
    your_grade = int(input())
    grade_list.append(your_grade)
print(grade_list)
print(grade_fix(grade_list, grade))
