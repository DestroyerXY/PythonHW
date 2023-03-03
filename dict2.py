# Вторая задача:
# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков

#     Напишите программу, которая вычисляет стоимость введенного пользователем слова.
#     Будем считать, что на вход подается только одно слово, которое содержит либо
#     только английские, либо только русские буквы.

#     ноутбук
#     12
# import re

# my_dict = { '[А, В, Е, И, Н, О, Р, С, Т]' : '[1]', '[Д, К, Л, М, П, У]' : '[2]', '[Б, Г, Ё, Ь, Я]' : '[3]', '[Й, Ы]' : '[4]', '[Ж, З, Х, Ц, Ч]' : '[5]', '[Ш, Э, Ю]' : '[8]', '[Ф, Щ, Ъ]' : '[10]'  }
# print(my_dict)
# w = input('Введите слово:')
# for k in my_dict:
#     w = re.sub(k, my_dict[k], w)
# print(sum(map(int, w)))

eng = {1:'AEIOULNSTR',
      	2:'DG',
      	3:'BCMP',
      	4:'FHVWY',
      	5:'K',
      	8:'JZ',
      	10:'QZ'}
rus = {1:'АВЕИНОРСТ',
      	2:'ДКЛМПУ',
      	3:'БГЁЬЯ',
      	4:'ЙЫ',
      	5:'ЖЗХЦЧ',
      	8:'ШЭЮ',
      	10:'ФЩЪ'}
N = abs(int(input('Введите 1 дл английского языка, 0 для русского: ')))
word = input('ВВЕДИТЕ СЛОВО БОЛЬШИМИ БУКВАМИ: ')
if N == 1:
    print(sum([k for i in word for k, v in eng.items() if i in v]))
elif N == 0:
    print(sum([k for i in word for k, v in rus.items() if i in v]))
else:
    print('Раскладка не соответствует слову')

# Семинар не досмотрел, в итоге нашел решение в интернете, так как не представлял как делать. Списал, буду разбираться, сдаю просто чтобы оппасть в дедлайн