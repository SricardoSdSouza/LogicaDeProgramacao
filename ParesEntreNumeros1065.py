'''
Faça um programa que leia 5 valores inteiros. Conte quantos destes valores digitados são pares e mostre esta informação.

Entrada = O arquivo de entrada contém 5 valores inteiros quaisquer.

Saída = Imprima a mensagem conforme o exemplo fornecido, indicando a quantidade de valores pares lidos.

Exemplo de Entrada	                  Exemplo de Saída
7                                           3 valores pares
-5
6
-4
12
'''
cont = 0
valores = [float(input()) for _ in range(5)]
for n in valores:
    if n % 2 == 0:
        cont += 1
print(f'{cont} valores pares')