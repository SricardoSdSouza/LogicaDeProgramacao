'''
Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e
informe-o expresso no formato horas:minutos:segundos.
Entrada
O arquivo de entrada contém um valor inteiro N.
Saída
Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:segundos, conforme exemplo fornecido.
Exemplo de Entrada	Exemplo de Saída
556      0:9:16

1        0:0:1

140153   38:55:53
'''
tempo = int(input('Informe o tempo em segundos: '))
hora = tempo // 60**2
tempo = tempo - hora * 60**2
minutos = tempo // 60
tempo = tempo - minutos * 60
segundos = tempo

#print(f'{hora}:{minutos}:{segundos}')
print(f'{hora:.0f}:{minutos:.0f}:{segundos:.0f}')

'''n = int(input())
h = n // 60**2
n = n - h * 60**2

m = n // 60
n = n - m*60

s = n'''
