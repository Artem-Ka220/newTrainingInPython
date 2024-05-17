"""
№2
Задача №27. Решение в группах
Пользователь вводит текст(строка). Словом считается
последовательность непробельных символов идущих
подряд, слова разделены одним или большим числом
пробелов. Определите, сколько различных слов
содержится в этом тексте.
Input: She sells sea shells on the sea shore
The shells that she sells are sea shells I'm sure.
So if she sells sea shells on the sea shore
I'm sure that the shells are sea shore shells
Output: 13
"""


#МОЙ

import re

your_sentence_text = input('Введите ваше предложение: ')
print(your_sentence_text)

plist = []

for i in your_sentence_text.split():
    if i.lower() not in plist:
        plist.append(i.lower())

print(plist)

count = 0
for i in plist:
    count += 1

print(count)

#ТВОЁ

data = """She sells sea shells on the sea shore The shells
that she sells are sea shells I'm sure.So if she sells sea
shells on the sea shore I'm sure that the shells are sea
shore shells""".lower().split()
print(len(list(set(data))))