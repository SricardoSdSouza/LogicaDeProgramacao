'''FATORIAL'''
n = int(input('Informe um número: '))
c = n
f = 1
while c > 0:
    if c > 1:
        print(f'{c}! x ', end='')
        f = f * c
        c -= 1
    else:
        break
#print(f'O fatorial de {n}! é = {f}')
print(f'1! = {f}')