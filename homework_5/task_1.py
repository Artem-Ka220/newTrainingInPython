#Напишите функцию f, которая на вход принимает два числа a и b, и возводит число a в целую степень b #с помощью рекурсии.

#Функция не должна ничего выводить, только возвращать значение.
#a = 3; b = 5 -> 243 (3⁵)
#a = 2; b = 3 -> 8 
def f(a, b):
    if b == 1:
        return a
    else:
        return (a * f(a, b - 1))

a,b = 2, 3
print(f(a,b))