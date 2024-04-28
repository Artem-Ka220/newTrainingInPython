array = [21, 25, 56, 89, 1, 78, 89]
print(array)
last = array.pop()
first = array.pop(0)

array.insert(0, last)
array.append(first)

print(array)