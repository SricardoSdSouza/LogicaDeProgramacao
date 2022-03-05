'''
Leia 100 valores inteiros. Apresente então o maior valor lido e a posição dentre os 100 valores lidos.
Entrada = O arquivo de entrada contém 100 números inteiros, positivos e distintos.
Saída = Apresente o maior valor lido e a posição de entrada, conforme exemplo abaixo.
Exemplo de Entrada	                Exemplo de Saída
2                                       34565
113                                     4
45
34565
6
...
8
'''
numeros = dict()
maior = 0
for i in range(100):
    n = int(input())
    if n > maior:
        maior = n
        numeros[n] = i # acicionará o valor como key do dicionário e gurardará a posição como valor

print(maior)
print(numeros[maior]+1) # imprime o valor da posição (se o indice 0 = posição 1, por isso soma + 1 ao fim)
