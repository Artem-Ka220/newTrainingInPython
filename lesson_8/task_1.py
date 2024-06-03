# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной
from csv import DictReader, DictWriter
from os.path import exists
import shutil

class NameError(Exception):
    def __init__(self, txt):
       self.txt = txt

def get_info():
    flag = False
    while not flag:
        try:
            first_name = input('Name: ')
            if len(first_name) < 2:
                raise NameError('The name is too short.')
            second_name = input('Enter last name:')
            if len(second_name) < 5:
                raise NameError('Last name too short.')
            phone_number = input('Enter your phone number.')
            if len(phone_number) < 11:
                raise NameError('The phone number is too short.')
        except NameError as err:
            print(err)
        else:
            flag = True
    return [first_name, second_name, phone_number]

def create_file(file_name):
    with open(file_name, 'w', encoding='utf-8', newline = '') as data:
        f_w = DictWriter(data, fieldnames=['Name','Surname', 'Phone'])
        f_w.writeheader()

def write_file(file_name):
    user_data = get_info()
    res = read_file(file_name)
    new_obj = {'first_name': user_data[0], 'second_name': user_data[1], 'phone_number': user_data[2]}
    res.append(new_obj)
    standart_write(file_name, res)

def read_file(file_name):
    with open(file_name, encoding='utf-8') as data:
        f_r = DictReader(data)
        return list(f_r) #ящик со словарями

def remove_row(file_name):
    search = int(input('Enter the phone number to delete: '))
    res = read_file(file_name)
    if search > len(res):
        res.pop(search - 1)
        standart_write(file_name, res)
    else:
        print('Invalid number entered.')
        
def standart_write(file_name, res):
    with open(file_name, 'w', encoding='utf-8', newline = '') as data:
        f_w = DictWriter(data, fieldnames=['first_name','second_name', 'phone_number'])
        f_w.writeheader()
        f_w.writerows(res)
        
def copy_data(new_file_name, res):
    with open(new_file_name, 'w') as data:
        f_w = standart_write(data, res)
   
file_name = 'phone.csv'
new_file_name = 'new_phone.csv'
def main():
    while True:
        command = input('Enter the command:')
        if command == 'q':
            break
        elif command == 'w':
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name)
        elif command == 'r':
            if not exists(file_name):
                print('The file is missing, please create it.')
                continue
            print(*read_file(file_name))
        elif command == 'd':
            if not exists(file_name):
                print('The file is missing, please create it.')
                continue
            remove_row(file_name)
        elif command == 'c':
            if not exists(new_file_name):
                create_file(new_file_name)
            shutil.copyfile(file_name, new_file_name)

            
            
 
 
main()


# Реализовать копирование данных из файла А в файл В
# Написать отдельную функцию copy_data
# Прочитать список словарей
# И записать его в новый файл использую функцию standart_write
# И дополнить функцию main()
# Из phone.csv  в phone2.csv
