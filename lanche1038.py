'''
Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item.
A seguir, calcule e mostre o valor da conta a pagar.
    Codigo        Especificação          Preço
      1           Cachorro Quente        R$ 4,00
      2           X-Salada               R$ 4,50
      3           X-Bacon                R$ 5,00
      4           Torrada Simples        R$ 2,00
      5           Refrigerante           R$ 1,50
Entrada
O arquivo de entrada contém dois valores inteiros correspondentes ao código e à quantidade de um item
conforme tabela acima.
Saída
O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, com 2 casas após o ponto decimal.
Exemplo de Entrada	Exemplo de Saída
3 2     Total: R$ 10.00

4 3     Total: R$ 6.00

2 3     Total: R$ 13.50
'''
entrada = input().split()
cod = int(entrada[0])
qtda = int(entrada[1])
if cod == 1:
    print(f'Total: R$ {qtda*4:.2f}')
elif cod == 2:
    print(f'O Total: R$ {qtda * 4.5:.2f}')
elif cod == 3:
    print(f'Total: R$ {qtda * 5:.2f}')
elif cod == 4:
    print(f'Total: R$ {qtda * 2:.2f}')
elif cod == 5:
    print(f'O Total: R${qtda * 1.5:.2f}')