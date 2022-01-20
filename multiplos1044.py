'''
Leia 2 valores inteiros (A e B). Após, o programa deve mostrar uma mensagem "Sao Multiplos" ou "Nao sao Multiplos",
indicando se os valores lidos são múltiplos entre si.
Entrada
A entrada contém valores inteiros.
Saída
A saída deve conter uma das mensagens conforme descrito acima.
Exemplo de Entrada	Exemplo de Saída
6 24    Sao Multiplos
6 25    Nao sao Multiplos
'''
x = input().split()
a, b = x
a = int(a)
b = int(b)
if a > b:
    if a % b == 0:
        print('São multiplos')
    else:
        print('Não são multiplos')
if a < b:
    if b % a == 0:
        print('São multiplos')
    else:
        print('Não São multiplos')
if a == b:
    print('São multiplos')
