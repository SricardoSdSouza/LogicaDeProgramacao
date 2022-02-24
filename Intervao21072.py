'''
Leia um valor inteiro N. Este valor será a quantidade de valores inteiros X que serão lidos em seguida.
Mostre quantos destes valores X estão dentro do intervalo [10,20] e quantos estão fora do intervalo, mostrando essas informações.
Entrada = A primeira linha da entrada contém um valor inteiro N (N < 10000), que indica o número de casos de teste.
Cada caso de teste a seguir é um valor inteiro X (-107 < X <107).
Saída = Para cada caso, imprima quantos números estão dentro (in) e quantos valores estão fora (out) do intervalo.
Exemplo de Entrada	            Exemplo de Saída
4                                   2 in
14                                  2 out
123
10
-25
'''
numeros_in = 0
numeros_out = 0
numero = int(input())
if numero < 10000:
    for i in range (numero):
        seq = int(input())
        if (-107 < seq < 107):
            if seq >= 10 and seq <= 20:
                numeros_in += 1
            else:
                numeros_out += 1
        else:
            numeros_out += 1


print(f'{numeros_in} in')
print(f'{numeros_out} out')

'''Outra forma'''
x = int(input())
_in = _out = 0
for num in range(x):
    n = int(input())
    if 0 <= n <= 20:
        _in += 1
    else:
        _out += 1

print('{} in'.format(_in))
print('{} out'.format(_out))