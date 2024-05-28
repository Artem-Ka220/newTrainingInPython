# Напишите функцию, которая принимает строку текста.
# Сформируйте список с уникальными кодами Unicode каждого
# симфола введённой строки отсортированный по убыванию.

def func(data):
    return sorted(set([ord(i) for i in data]), reverse=True)

print(func('kdjasdlkfj;dasdlksjf;df'))