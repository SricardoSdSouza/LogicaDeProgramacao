''' Encontre todos os números promos de 2 até n'''
'''Pegar o ultimo numeros e tirar sua raiz arredondando para baixo'''

'''
raiz = 10 ** (1/2) 
print(raiz)
# vai dar um número 3.1623.1622776601683795'''
'''
from math import floor
raiz = floor(10 ** (1/2))
print(raiz)
# vai dar um número 3'''
# colocando em codigo
from math import floor
import time
def crivo(n):
    numeros = list(range(2, n+1))
    # Assuminto que todos são numeros primos para depois testa-los
    is_primo = [True] * (n -1)

    # achando a raiz do último numero
    maximo_calcular = floor(numeros[-1] **(1/2))
    # fazer um for para obeter os numeros que serão testados
    for i in range(2, maximo_calcular + 1):
        for j in numeros:
            if i != j:
                if j % i == 0:
                    is_primo[j-2] = False
    primos = [numeros[i] for i,j in enumerate(is_primo) if j == True]
    return primos

start = time.time()
primos =(crivo(30))
end = time.time()
print(f'Tempo: {end - start}')
print(primos)