'''
Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. Se não for
possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”, caso haja uma divisão
por 0 ou raiz de numero negativo.
Entrada
Leia três valores de ponto flutuante (double) A, B e C.
Saída
Se não houver possibilidade de calcular as raízes, apresente a mensagem "Impossivel calcular".
Caso contrário, imprima o resultado das raízes com 5 dígitos após o ponto, com uma mensagem correspondente
conforme exemplo abaixo. Imprima sempre o final de linha após cada mensagem.

Exemplos de Entrada	Exemplos de Saída
10.0 20.1 5.1    R1 = -0.29788
                 R2 = -1.71212

0.0 20.0 5.0     Impossivel calcular

10.3 203.0 5.0   R1 = -0.02466
                 R2 = -19.68408

10.0 3.0 5.0     Impossivel calcula
'''
import math

raizes = input().split()
a = float(raizes[0])
b = float(raizes[1])
c = float(raizes[2])
d = (b*b - (4*a*c))

if a == 0:
    print('Impossível calcular')
elif d < 0 :
    print('Impossível calcular')
elif d > 0:
    delta = math.sqrt(d)
    r1 = (-b + delta)/(2 * a)
    print(f'R1 = {r1:.5f}')
    r2 = (-b - delta)/(2 * a)
    print(f'R2 = {r2:.5f}')