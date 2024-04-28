#В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.

#В случае с английским алфавитом очки распределяются так:

#A, E, I, O, U, L, N, S, T, R – 1 очко;
#D, G – 2 очка;
#B, C, M, P – 3 очка;
#F, H, V, W, Y – 4 очка;
#K – 5 очков;
#J, X – 8 очков;
#Q, Z – 10 очков.
#А русские буквы оцениваются так:

#А, В, Е, И, Н, О, Р, С, Т – 1 очко;
#Д, К, Л, М, П, У – 2 очка;
#Б, Г, Ё, Ь, Я – 3 очка;
#Й, Ы – 4 очка;
#Ж, З, Х, Ц, Ч – 5 очков;
#Ш, Э, Ю – 8 очков;
#Ф, Щ, Ъ – 10 очков.
#Напишите программу, которая вычисляет стоимость введенного пользователем слова k и выводит его.
#Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
k = 'qzфщъ'
# 12

letters = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т']
letters_1 = ['D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У']
letters_2 = ['B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я']
letters_3 = ['F', 'H', 'V', 'W', 'Y', 'Й', 'Ы']
letters_4 = ['K', 'Ж', 'З', 'Х', 'Ц', 'Ч']
letters_5 = ['J', 'X', 'Ш', 'Э', 'Ю']
letters_6 = ['Q', 'Z', 'Ф', 'Щ', 'Ъ']

score = 0

for el in k:
    if el.upper() in letters:
        score += 1
    elif el.upper() in letters_1:
        score += 2
    elif el.upper() in letters_2:
        score += 3
    elif el.upper() in letters_3:
        score += 4
    elif el.upper() in letters_4:
        score += 5
    elif el.upper() in letters_5:
        score += 8
    else:
        score += 10
print(score)
