'''
Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e
calcule a distância entre eles, mostrando 4 casas decimais após a vírgula, segundo a fórmula:

Distancia =

Entrada
O arquivo de entrada contém duas linhas de dados. A primeira linha contém dois valores de ponto flutuante:
x1 y1 e a segunda linha contém dois valores de ponto flutuante x2 y2.

Saída
Calcule e imprima o valor da distância segundo a fórmula fornecida, com 4 casas após o ponto decimal.

Exemplo de Entrada	Exemplo de Saída
1.0 7.0
5.0 9.0            4.4721

-2.5 0.4
12.1 7.3           16.1484

2.5 -0.4
-12.2 7.0          16.4575
'''

import math
from math import sqrt

x = input().split()
y = input().split()

x1 = float(x[0])
y1 = float(x[1])

x2 = float(y[0])
y2 = float(y[1])

calc = sqrt((x2-x1)*(x2-x1) + ((y2 - y1)*(y2 - y1)))
#print(f'{calc:.4f}')
print(f'{sqrt((x2-x1)*(x2-x1) + ((y2 - y1)*(y2 - y1))):.4f}')