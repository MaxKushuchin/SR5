def conv(n, m):
    b = ''
    while n > 0:
        b = str(n % m) + b
        n //= m
    print(b.rjust(8, '0'))



n = int(input('Введите число: '))
m = int(input('Введите целевую систему счисления: '))
if m == 2 or m == 8:   
    conv(n, m)
