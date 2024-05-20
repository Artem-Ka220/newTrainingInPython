#Задача №35. Решение в группах
#Напишите функцию, которая принимает одно число и
#проверяет, является ли оно простым
#Напоминание: Простое число - это число, которое
#имеет 2 делителя: 1 и n(само число)

def prime_number(any_number,count):
    if any_number % count == 0:
        return count
    else:
        count += 1
        return prime_number(any_number,count)

your_num = int(input("What number do you want to check?"))

any_new_num = prime_number(your_num, 2)
print(any_new_num)
if any_new_num == your_num:
    print('Yes')
else:
    print('No')


#2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131,
#137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293,
