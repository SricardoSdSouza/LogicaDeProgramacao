'''
Leia um valor inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste de dois
inteiros X e Y. Você deve apresentar a soma de todos os ímpares existentes entre X e Y.
Entrada = A primeira linha de entrada é um inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso
de teste consiste em uma linha contendo dois inteiros X e Y.
Saída = Imprima a soma de todos valores ímpares entre X e Y.

Exemplo de Entrada	            Exemplo de Saída
7
4 5                                 0
13 10                               11
6 4                                 5
3 3                                 0
3 5                                 0
3 4                                 0
3 8                                 12
'''
entrada = int(input())

for i in range(entrada):
    impar = 0
    num = input().split()
    x = int(num[0])
    y = int(num[1])
    if x > y:
        x, y = y, x
    for i in range(x+1, y):
        if i % 2 != 0:
            impar += i
    print(impar)
'''OU assim
def soma(a, b):
	if a > b:
	   a, b = b, a
	return sum([i for i in range(a+1,b) if i%2 != 0])

n = int(input())
for i in range(n):
	x,y = list(map(int, input().split()))
	print(soma(x, y))
'''