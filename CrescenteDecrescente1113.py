'''
Leia uma quantidade indeterminada de duplas de valores inteiros X e Y. Escreva para cada X e Y uma mensagem que indique
se estes valores foram digitados em ordem crescente ou decrescente.
Entrada = A entrada contém vários casos de teste. Cada caso contém dois valores inteiros X e Y. A leitura deve ser
encerrada ao ser fornecido valores iguais para X e Y.
Saída = Para cada caso de teste imprima “Crescente”, caso os valores tenham sido digitados na ordem crescente,
caso contrário imprima a mensagem “Decrescente”.

Exemplo de Entrada	                    Exemplo de Saída
5 4                                         Decrescente
7 2                                         Decrescente
3 8                                         Crescente
2 2
'''
continua = True
while continua == True:
    valor = input().split()
    x = int(valor[0])
    y = int(valor[1])
    if x == y:
        break
    if x > y:
        print('Decrescente')
    elif x < y:
        print('Crescente')

'''Ou assim
while True:
    valores = [int(i) for i in input().split()]
    x, y = valores
    if x == y:
        break
    elif x > y:
        print('Decrescente')
    else:
        print('Crescente')'''