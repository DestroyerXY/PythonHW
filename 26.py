# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

Num = int(input('Введите число:'))
Deg = int(input('Введите степень:'))

def recNpowD(Num, Deg):
    if Deg == 0:
        return 1
    return Num * recNpowD(Num, Deg - 1)

print (recNpowD(Num,Deg))