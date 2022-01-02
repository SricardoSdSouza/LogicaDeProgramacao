'''
Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1,
o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre
o valor a ser pago.

Entrada
O arquivo de entrada contém duas linhas de dados. Em cada linha haverá 3 valores,
respectivamente dois inteiros e um valor com 2 casas decimais.
ex:
12 1 5.30
16 2 5.10          VALOR A PAGAR: R$ 15.50

13 2 15.30
161 4 5.20         VALOR A PAGAR: R$ 51.40
'''
'''código_peça_1 = int(input('Informe cd 1: '))
número_peça_1 = int(input('Informe num 1: '))
valor_peça_1 =  float(input('Informe valor 1: '))
código_peça_2 = int(input('Informe cd 2: '))
número_peça_2 = int(input('Informe num 2: '))
valor_peça_2 =  float(input('Informe valor 2: '))
valor_a_pagar = ( número_peça_1 * valor_peça_1 ) + ( número_peça_2 * valor_peça_2 )
print("VALOR A PAGAR = R$ %.2f" %valor_a_pagar)'''

'''cd_peca1 = int(input('1: '))
num_peca1 = int(input('1: '))
val_peca1 = float(input('1: '))
cd_peca2 = int(input('2: '))
num_peca2 = int(input('2: '))
val_peca2 = float(input('2: '))
print(f'VALOR A PAGAR: R$ {(num_peca1*val_peca1)+(num_peca2*val_peca2):.2f}')'''


'''entrada1 = input()
entrada2 = input()
valor1 = int(entrada1[2])
valor11 =float(entrada1[3:])
valor2 = int(entrada2[2])
valor22 =float(entrada2[3:])
v1 = valor1*valor11
v2 = valor2*valor22
print(v1)
print(v2)
print(f'VALOR A PAGAR: R$ {v1+v2:.2f}')'''

entrada1 = input().split()
entrada2 = input().split()
n1, n2, n3 =entrada1
m1, m2, m3 =entrada2
v1 = int(n2)*float(n3)
v2 = int(m2)*float(m3)
print(f'VALOR A PAGAR: R$ {v1+v2}')