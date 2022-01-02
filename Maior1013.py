'''
Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”.
Utilize a fórmula:
Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b). Um segundo passo, portanto é necessário para
chegar no resultado esperado.
Entrada
O arquivo de entrada contém três valores inteiros.
Saída
Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".
Exemplos de Entrada	Exemplos de Saída
7 14 106      106 eh o maior

217 14 6      217 eh o maior
'''
entrada = input().split()
a = int(entrada[0])
b = int(entrada[1])
c = int(entrada[2])
if a > b and a > c:
    print(f'{a} eh o maior')
if b > a and b > c:
    print(f'{b} eh 0 maior')
if c > a and c > b:
    print(f'{c} eh o maior')

import math

valor = input().split(" ")

a, b, c = valor

maior = (int(a) + int(b) + abs(int(a) - int(b)))  / 2
resultado = (int(maior) + int(c) + abs(int(maior) - int(c)))/2

#print("%d eh o maior" %resultado)
print(f'{resultado:.0f} eh o maior')