temp1 = temp2 = 1
 
N = int(input()) 
for i in range(2, N+1):
    temp1, temp2 = temp2, temp1 + temp2
print(temp2)

#Последовательность Фибоначи задается следующим образом: каждый следующий элемент является суммой двух предыдущих.

#Начало выглядит так: 1, 1, 2, 3, 5, 8, 13, 21, 34, ... Напишите программу, которая выводит n-ый элемент этой

#последовательности.

#Входные данные: n - номер числа последовательности

#Выходные данные: F(n) - n-ое число из последовательности

#Пример входных данных: 10

#Пример выходных данных: 89
