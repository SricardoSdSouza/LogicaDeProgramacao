'''
Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente,
uma linha em branco e em seguida, os valores na sequência como foram lidos.
Entrada
A entrada contem três números inteiros.
Saída
Imprima a saída conforme foi especificado.

Exemplo de Entrada	          Exemplo de Saída
7 21 -14                         -14
                                  7
                                  21

                                  7
                                  21
                                 -14

-14 21 7                         -14
                                  7
                                  21

                                 -14
                                  21
                                  7
'''
num = input().split()
a, b, c = num
a = int(a)
b = int(b)
c = int(c)
if a > b and a > c:
    d = a# maior valor = d
    if b > c:
        e = b
        f = c
    else:
        e = c
        f = b

if b > a and b > c:
    d = b
    if a > c:
        e = a
        f = c
    else:
        e = c
        f = a
if c > a and c > b:
    d = c
    if a > b:
        e = a
        f = b
    else:
        f = a
        e = b

print(f)
print(e)
print(d)
print()
print(a)
print(b)
print(c)
