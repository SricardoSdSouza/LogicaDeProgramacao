'''
Leia um valor inteiro X. Em seguida apresente os 6 valores ímpares consecutivos a partir de X, um valor por linha,
inclusive o X ser for o caso.

Entrada = A entrada será um valor inteiro positivo.

Saída = A saída será uma sequência de seis números ímpares.

Exemplo de Entrada	       Exemplo de Saída
8                               9
                                11
                                13
                                15
                                17
                                19
'''
numero = int(input())
for x in range(numero + 5):
    if not numero % 2 == 0:
        print(numero)
    numero += 1
'''Outra forma
impares = int(input())
for i in range(impares, impares+12):  # se quero 6 números, então fui até o dobro (12)
    if i % 2 != 0:
        print(i)
'''