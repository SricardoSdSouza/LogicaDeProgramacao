'''
A empresa ABC resolveu conceder um aumento de salários a seus funcionários de acordo com a tabela abaixo:


        Salário	                      Percentual de Reajuste
        0 - 400.00                          15%
        400.01 - 800.00                     12%
        800.01 - 1200.00                    10%
        1200.01 - 2000.00                    7%
        Acima de 2000.00                     4%


Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste ganho e o
índice reajustado, em percentual.

Entrada = A entrada contém apenas um valor de ponto flutuante, com duas casas decimais.

Saída = Imprima 3 linhas na saída: o novo salário, o valor ganho de reajuste e o percentual de reajuste ganho,
conforme exemplo abaixo.

Exemplo de Entrada	               Exemplo de Saída
    400.00                             Novo salario: 460.00
                                       Reajuste ganho: 60.00
                                       Em percentual: 15 %

    800.01                             Novo salario: 880.01
                                       Reajuste ganho: 80.00
                                       Em percentual: 10 %

    2000.00                            Novo salario: 2140.00
                                       Reajuste ganho: 140.00
                                       Em percentual: 7 % '''
valor = float(input())
if valor < 0:
    exit
elif valor <= 400:
    reajuste = valor * 0.15
    salario = valor + reajuste
    print(f'Novo salario: {salario:.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}')
    print(f'Em percentual: 15 %')
elif valor <= 800.00:
    reajuste = valor * 0.12
    salario = valor + reajuste
    print(f'Novo salario: {salario:.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}')
    print(f'Em percentual: 12 %')
elif valor <= 1200.00:
    reajuste = valor * 0.10
    salario = valor + reajuste
    print(f'Novo salario: {salario:.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}')
    print(f'Em percentual: 10 %')
elif valor <= 2000.00:
    reajuste = valor * 0.07
    salario = valor + reajuste
    print(f'Novo salario: {salario:.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}')
    print(f'Em percentual: 7 %')
elif valor > 2000.00:
    reajuste = valor * 0.04
    salario = valor + reajuste
    print(f'Novo salario: {salario:.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}')
    print(f'Em percentual: 4 %')