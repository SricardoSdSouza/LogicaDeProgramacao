'''
Faça um programa que leia 6 valores. Estes valores serão somente negativos ou positivos (desconsidere os valores nulos).
 A seguir, mostre a quantidade de valores positivos digitados.
Entrada = Seis valores, negativos e/ou positivos.
Saída = Imprima uma mensagem dizendo quantos valores positivos foram lidos.

Exemplo de Entrada          	Exemplo de Saída
7                                   4 valores positivos
-5
6
-3.4
4.6
12
'''
positivo = 0
for i in range(6):
    valores = float(input())
    if valores > 0:
        positivo += 1

print(f'{positivo} valores positivos')

