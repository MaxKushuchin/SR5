def conv(n, m):
    b = ''
    while n > 0:
        b = str(n % m) + b
        n //= m
    return b



n = int(input('Введите число: '))
m = int(input('Введите целевую систему счисления: '))
if m == 2 or m == 8:
    result = conv(n, m)
    if len(result) != 8:
        result = '0' * (8-len(result)) + result
        print(n, '->' , result)
