#Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в 
#порядке возрастания все те числа, которые встречаются в обоих наборах.
#На вход подается 2 числа через пробел: n m
#n - кол-во элементов первого множества.
#m - кол-во элементов второго множества.
#Затем подаются элементы каждого множества через пробел в виде строки. ! Писать input() не надо

#var1 = '5 4' # количество элементов первого и второго множества
#var2 = '1 3 5 7 9' # элементы первого множества через пробел
#var3 = '2 3 4 5' # элементы второго множества через пробел

#3 5

var1 = '9 10'
var2 = '1 3 5 7 9 8 99 -1 2 100 101 200 203'
var3 = '8 2 3 4 5 7 9 99 100 101'

list_one = list(var2.split())
list_two = list(var3.split())

var4 = []
if int(var1[0]) > int(var1[2]):
    for i in list_one:
        if i in list_two and i != ' ':
            if int(i) not in var4:
                var4.append(int(i))
else:
    for i in list_two:
        if i in list_one and i != ' ':
            if int(i) not in var4:
                var4.append(int(i))
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
        
new_list = quicksort(var4)
for i in new_list:
    print(i, end = ' ')
