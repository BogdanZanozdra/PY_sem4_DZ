# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# "20" -> [2, 2, 5]

simple_numbers = []
def prime(x):
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

for number in range(1,100):
    if prime(number ):
        simple_numbers.append(number)k
        
# print(simple_numbers)    

n = int(input('Задайте натуральное число: '))
for i in simple_numbers[1:]:
    while n % i == 0:
        n = n / i
        print(i, end=' ')

