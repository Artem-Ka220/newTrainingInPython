# Реализовать функцию,принимающую несколько параметров,описывающих данные пользователя:
# имя, фамилия, год рождения, город проживание,email, телефон.
# Функция должна принимать параметры как именнованные аргументы.
# Реализовать вывод данных о пользователи одной строкой.

# Пример: Иванов Иван 1846 года рождения, проживает в городе Москва.
# email: jackie@email.com, телефон: 895623

def func(**kwargs):
    return f'employee: {kwargs['name']} {kwargs['surname']}, {kwargs['age']}'

print(func(name='Ivan', surname='Ivanov', age='25'))