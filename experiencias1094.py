'''
Maria acabou de iniciar seu curso de graduação na faculdade de medicina e precisa de sua ajuda para organizar os
experimentos de um laboratório o qual ela é responsável. Ela quer saber no final do ano, quantas cobaias foram utilizadas
no laboratório e o percentual de cada tipo de cobaia utilizada.Este laboratório em especial utiliza três tipos de
cobaias: sapos, ratos e coelhos.
Para obter estas informações, ela sabe exatamente o número de experimentos que foram realizados, o tipo de cobaia
utilizada e a quantidade de cobaias utilizadas em cada experimento.
Entrada = A primeira linha de entrada contém um valor inteiro N que indica os vários casos de teste que vem a seguir.
Cada caso de teste contém um inteiro Quantia (1 ≤ Quantia ≤ 15) que representa a quantidade de cobaias utilizadas e um
caractere Tipo ('C', 'R' ou 'S'), indicando o tipo de cobaia (R:Rato S:Sapo C:Coelho).

Saída = Apresente o total de cobaias utilizadas, o total de cada tipo de cobaia utilizada e o percentual de cada uma em
relação ao total de cobaias utilizadas, sendo que o percentual deve ser apresentado com dois dígitos após o ponto.

Exemplo de Entrada	      Exemplo de Saída
10                          Total: 92 cobaias
10 C                        Total de coelhos: 29
6 R                         Total de ratos: 40
15 S                        Total de sapos: 23
5 C                         Percentual de coelhos: 31.52 %
14 R                        Percentual de ratos: 43.48 %
9 C                         Percentual de sapos: 25.00 %
6 R
8 S
5 C
14 R
'''
qtda = int(input())
q = 0
c = r = s = 0
totc = 0
totr = 0
tots = 0
soma = 0
for i in range(qtda):
    cobaia = input().split()
    expe =int(cobaia[0])
    animal = cobaia[1].upper()
    soma += expe
    if animal == 'C':
        c += 1
        totc += expe
    if animal == 'R':
        r += 1
        totr += expe
    if animal == 'S':
        s += 1
        tots += expe

print(f'Total: {soma} cobaias')
print(f'Total de coelhos: {totc}')
print(f'Total de ratos: {totr}')
print(f'Total de sapos: {tots}')
print(f'Percentual de coelhos: {(totc/soma)*100:.2f} %')
print(f'Percentual de ratos: {(totr/soma)*100:.2f} %')
print(f'Percentual de sapos: {(tots/soma)*100:.2f} %')
''' outra forma  
c = r = s = 0
n = int(input())
for i in range(n):
    opc = input().split()
    num, animal = opc
    if animal.upper() == 'C':
        c += int(num)
    elif animal.upper() == 'R':
        r += int(num)
    elif animal.upper() == 'S':
        s += int(num)
total = c + r + s
print('Total: {} cobaias'.format(total))
print('Total de coelhos: {}'.format(c))
print('Total de ratos: {}'.format(r))
print('Total de sapos: {}'.format(s))
print('Percentual de coelhos: {:.2f} %'.format(c / total * 100))
print('Percentual de ratos: {:.2f} %'.format(r / total * 100))
print('Percentual de sapos: {:.2f} %'.format(s / total * 100))
'''