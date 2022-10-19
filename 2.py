def conv(n, m):
    b = ''
    while n > 0:
        b = str(n % m) + b
        n //= m
    return b.rjust(8, '0') #создание восьмибитной записи числа



n = int(input('Введите число: '))
m = int(input('Введите целевую систему счисления: '))
if m == 2 or m == 8:
    print(n, '->' , conv(n, m))
