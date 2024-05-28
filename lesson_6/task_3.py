# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
def f(lst):
    count = 0
    for i in lst:
        for j in range(0, i):
            if lst[i] == lst[j]:
                count += 1
    print(count)

list_1 = [1, 2, 3, 2, 3, 3, 3, 3]
f(list_1)
#или
list_2 = [1, 2, 3, 2, 3, 3, 3, 3]
my_set = set(list_2)

print(my_set)
res = []
for item in my_set:
    res.append(list_2.count(item) // 2)
print(sum(res))

#или
print(sum([list_2.count(item) // 2 for item in set(list_2)]))