'''
Escreva um programa para ler as coordenadas (X,Y) de uma quantidade indeterminada de pontos no sistema cartesiano.
Para cada ponto escrever o quadrante a que ele pertence. O algoritmo será encerrado quando pelo menos uma de duas
coordenadas for NULA (nesta situação sem escrever mensagem alguma).

Entrada = A entrada contém vários casos de teste. Cada caso de teste contém 2 valores inteiros.

Saída = Para cada caso de teste mostre em qual quadrante do sistema cartesiano se encontra a coordenada lida,
conforme o exemplo.

Exemplo de Entrada	                Exemplo de Saída
2 2                                     primeiro
3 -2                                    quarto
-8 -1                                   terceiro
-7 1                                    segundo
0 2
'''
'''coordenadas = input().split()
x = int(coordenadas[0])
y = int(coordenadas[1])
if x == 0 or y == 0:
    exit
if x > 0 and y >0:
    print('primeiro')
elif x > 0 and y < 0:
    print('quarto')
elif x < 0 and y < 0:
    print('tereiro')
elif x < 0 and y > 0:
    print('segundo')'''

''' ou'''
while True:
    valores = [int(i) for i in input().split()]
    x, y = valores
    quadrante = {
                    x > 0 and y > 0 : 'primeiro',
                    x > 0 and y < 0: 'quarto',
                    x < 0 and y < 0: 'terceiro',
                    x < 0 and y > 0: 'segundo',
                }
    if x == 0 or y == 0:
        break
    for k, v in quadrante.items():
        if k:
            print(v)
