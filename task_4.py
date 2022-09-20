# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# 5. k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint, random

k = 5
mnogochlen = []
for i in range(k + 1):
    chlen = 's*x^k'
    d = randint(1, 9)
    n = str(d)
    temp =  list(chlen)
    temp[0] = n
    temp[-1] = str(k)
    if temp[-1] == '1':
        del temp[-2]
        del temp[-1]
    if temp[-1] == '0':
        del temp[-4:-1]
        del temp[-1]    
    # print(chlen)
    chlen = ''.join(temp)
    k = int(k)
    k -= 1
    mnogochlen.append(chlen)
    # print(chlen)
mnogochlen = ' + '.join(mnogochlen)
print(mnogochlen + ' = 0')

data = open('mnogochlen.txt', 'a')
data.writelines(mnogochlen)
data.close()