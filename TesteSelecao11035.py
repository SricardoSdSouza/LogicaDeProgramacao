'''Leia 4 valores inteiros A, B, C e D. A seguir, se B for maior do que C e se D for maior do que A, e a soma de
C com D for maior que a soma de A e B e se C e D, ambos, forem positivos e se a variável A for par escrever a mensagem
"Valores aceitos", senão escrever "Valores nao aceitos".

Entrada
Quatro números inteiros A, B, C e D.

Saída
Mostre a respectiva mensagem após a validação dos valores.

Exemplo de Entrada	Exemplo de Saída
5 6 7 8     Valores nao aceitos

2 3 2 6     Valores aceitos'''
'''numeros = input().split()
A = int(numeros[0])
B = int(numeros[1])
C = int(numeros[2])
D = int(numeros[3])
if B > C :
    if D > A:
        if (C + D) > (A + B):
            if C > 0:
                 if D > 0 and A %2==0:
                    print('Valores aceitos')
else:
    print('Valores não aceitos')'''

# pode ser assim:
numeros = input()
numeros = [int(x) for x in numeros.split()]
A = int(numeros[0])
B = int(numeros[1])
C = int(numeros[2])
D = int(numeros[3])
if B > C and D > A and (C + D) > (A + B) and C > 0 and D > 0 and A %2 == 0:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')