def conv(chislo, system):
    result = ''
    while chislo > 0:
        result = str(chislo % system) + result
        chislo //= system
    if len(result) != 8:
        result = '0' * (8-len(result)) + result
    print(result)
    
    



chislo = int(input('Введите число: '))
system = int(input('Введите целевую систему счисления: '))
if system == 2 or system == 8:   
    conv(chislo, system)
