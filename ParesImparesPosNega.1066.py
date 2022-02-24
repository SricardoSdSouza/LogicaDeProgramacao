'''
Leia 5 valores Inteiros. A seguir mostre quantos valores digitados foram pares, quantos valores digitados foram
ímpares, quantos valores digitados foram positivos e quantos valores digitados foram negativos.

Entrada = O arquivo de entrada contém 5 valores inteiros quaisquer.

Saída = Imprima a mensagem conforme o exemplo fornecido, uma mensagem por linha, não esquecendo o final de
linha após cada uma.

Exemplo de Entrada	             Exemplo de Saída
-5                                  3 valor(es) par(es)
0                                   2 valor(es) impar(es)
-3                                  1 valor(es) positivo(s)
-4                                  3 valor(es) negativo(s)
12
'''
par = 0
imp = 0
pos = 0
neg = 0
valores = [float(input()) for _ in range(5)]
for n in valores:
    if n == 0:
        par += 1
        continue
    if n % 2 == 0 and n > 0:
        par += 1
        pos += 1
        continue
    if n % 2 == 0 and n < 0:
        par += 1
        neg += 1
        continue
    else:
        if n < 0:
            neg += 1
            imp += 1
        else:
            pos += 1
            imp += 1
print(f'{par} valor(es) par(es)')
print(f'{imp} valor(es) impar(es)')
print(f'{pos} valor(es) positivo(s)')
print(f'{neg} valor(es) negativo(s)')

