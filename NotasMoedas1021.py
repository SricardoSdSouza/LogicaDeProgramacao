'''
Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).
Saída
Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, conforme exemplo fornecido.
Obs: Utilize ponto (.) para separar a parte decimal.
Exemplo de Entrada	Exemplo de Saída
576.73   NOTAS:
                5 nota(s) de R$ 100.00
                1 nota(s) de R$ 50.00
                1 nota(s) de R$ 20.00
                0 nota(s) de R$ 10.00
                1 nota(s) de R$ 5.00
                0 nota(s) de R$ 2.00
        MOEDAS:
                1 moeda(s) de R$ 1.00
                1 moeda(s) de R$ 0.50
                0 moeda(s) de R$ 0.25
                2 moeda(s) de R$ 0.10
                0 moeda(s) de R$ 0.05
                3 moeda(s) de R$ 0.01
'''
n = float(input('Informe o valor que deseja decompor: R$  '))
m = n
print(f'o valor a ser decomposto é R${n}')
n100 = n // 100
n = n - n100*100

n50 = n // 50
n = n - n50*50

n20 = n // 20
n = n - n20*20

n10 = n // 10
n = n - n10*10

n5 = n // 5
n = n - n5*5

n2 = n // 2
n = n - n2*2

m1 = n // 1
m = n - m1*1

m2 = m // 0.5
m = m - m2*0.5

m3 = m // 0.25
m = m - m3*0.25

m4 = m // 0.10
m = m - m4*0.10

m5 = m // 0.05
m = m - m5*0.05

m6 = m // 0.01
m = m - m6*0.01
print('NOTAS:')
print(f'Foram {n100} nota(s) de R$ 100,00')
print(f'Foram {n50} nota(s) de R$ 50,00')
print(f'Foram {n20} nota(s) de R$ 20,00')
print(f'Foram {n10} nota(s) de R$ 10,00')
print(f'Foram {n5} nota(s) de R$ 5,00')
print(f'Foram {n2} nota(s) de R$ 2,00')
print('Moedas:')
print(f'Foram {m1} moeda(s) de R$ 1,00')
print(f'Foram {m2} moeda(s) de R$ 0,50')
print(f'Foram {m3} moeda(s) de R$ 0,25')
print(f'Foram {m4} moeda(s) de R$ 0,10')
print(f'Foram {m5} moeda(s) de R$ 0,05')
print(f'Foram {m6} moeda(s) de R$ 0,01')