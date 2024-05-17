"""
Задача №29. Решение в группах
Ваня и Петя поспорили, кто быстрее решит
следующую задачу: “Задана последовательность
неотрицательных целых чисел. Требуется определить
значение наибольшего элемента
последовательности, которая завершается первым
встретившимся нулем (число 0 не входит в
последовательность)”. Однако 2 друга оказались не
такими смышлеными. Никто из ребят не смог до
конца сделать это задание. Они решили так: у кого
будет меньше ошибок в коде, тот и выиграл спор. За
помощью товарищи обратились к Вам, студентам.
Ваня:

n = int(input())
max_number = 1000
while n != 0:
 n = int(input())
 if max_number > n:
 max_number = n
print(max_number)

Петя:

n = int(input())
max_number = -1
while n < 0:
 n = int(input())
 if max_number < n:
 n = max_number
print(n)
"""

#МОЁ

max_number = 0
while True:
    enter_num = int(input("Enter any number: "))
    if max_number < enter_num:
        max_number = enter_num
    elif enter_num == 0:
        print(max_number)
        break

#ТВОЁ
