# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу.

# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами.

# Стихотворение  Винни-Пух передаст вам автоматически в переменную stroka в виде строки. В ответе напишите Парам пам-пам, если с ритмом все в порядке и Пам парам, если с ритмом все не в порядке.
# Если фраза только одна, то ритм определить не получится и необходимо вывести: Количество фраз должно быть больше одной!
# Пример

# На входе:
# stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
# На выходе:
# Парам пам-пам

#моё решение:
def rhytm(any_list, some_list):
    new_list = []
    if len(any_list) == 1:
        return 'Количество фраз должно быть больше одной!'
    else:
        for i in range(len(list_new)):
            new_list.append((list([item for item in list_new[i] if item in some_list])))

    for i in range(len(new_list)):
        if len(new_list[i]) != len(new_list[i - 1]):
            return 'Пам парам'
    return 'Парам пам-пам'

stroka = 'по-русски говорят'

vowels = ['а', 'я', 'у', 'ю', 'о', 'е', 'ё', 'э', 'и', 'ы' ]

list_new = list(stroka.split())

print(rhytm(list_new, vowels))

#эталонное решение:

vowels = ['а', 'е', 'ё', 'и', 'й', 'о', 'у', 'ы', 'э', 'ю', 'я']
phrases = stroka.split()
if len(phrases) < 2:
 print('Количество фраз должно быть больше одной!')
else:
 countVowels = []

 for i in phrases:
  countVowels.append(len([x for x in i if x.lower() in vowels]))

 if countVowels.count(countVowels[0]) == len(countVowels):
  print('Парам пам-пам')
 else:
  print('Пам парам')