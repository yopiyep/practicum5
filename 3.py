num =  int(input())
if num < 1000 or num > 9999:
    print('Неверно введено число!')
else:
    x1 = num // 1000
    x2 = (num % 1000) // 100
    x3 = (num % 100) // 10
    x4 = num % 10
if x1 == x4 and x3 == x2:
    print('настоящее')
else:
    print('кривое')