#Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех #арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

#Функция не должна ничего выводить, только возвращать значение.
#sum(2, 2)
# 4
def f_sum(a, b):
    if a == a + b:
        return a
    else:
        return f_sum(a + (b -(b - 1)), b - 1)
    
a, b = 50,89
print(f_sum(a,b))