"""
Задача №17. Решение в группах
Дан список чисел. Определите, сколько в нем
встречается различных чисел.
Input: [1, 1, 2, 0, -1, 3, 4, 4]
Output: 6
"""
nums = [1, 1, 2, 0, -1, 3, 4, 4]
print(nums)
print(len(set(nums)))
list_2 = []
for el in nums:
    if el not in list_2:
        list_2.append(el)

print(list_2)
print(len(list_2))