# Найдите сумму цифр трехзначного числа n.

# Результат сохраните в перменную res.
n = 159

res = (n % 10) + (n // 10 % 10) + (n // 100 % 10)
print(res)