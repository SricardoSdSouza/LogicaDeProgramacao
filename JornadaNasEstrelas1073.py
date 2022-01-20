'''
Após comprar vários sítios adjacentes na região do oeste catarinense, a família Estrela construiu uma única estrada
que passa por todos os sítios em sequência. O primeiro sítio da sequência foi batizado de Estrela 1, o segundo de
Estrela 2, e assim por diante. Porém, o irmão que vive em Estrela 1 acabou enlouquecendo e resolveu fazer uma Jornada
nas Estrelas para roubar carneiros das propriedades de seus irmãos. Mas ele está definitivamente pirado. Quando passa
pelo sítio Estrela i, ele rouba apenas um carneiro daquele sítio (se o sítio tem algum) e segue ou para Estrela i + 1
ou para Estrela i - 1, dependendo se o número de carneiros em Estrela i era, respectivamente, ímpar ou par. Se não
existe a Estrela para a qual ele deseja seguir, ele interrompe sua jornada. O irmão louco começa sua Jornada em
Estrela 1, roubando um carneiro do seu próprio sítio.
Entrada
A primeira linha da entrada consiste de um único inteiro N (1 ≤ N ≤ 106), o qual representa o número de Estrelas.
A segunda linha da entrada consiste de N inteiros, de modo que o i-ésimo inteiro, Xi (1 ≤ Xi ≤ 106), representa o
número inicial de carneiros em Estrela i.
Saída
Imprima uma linha contendo dois inteiros, de modo que o primeiro represente o número de Estrelas atacadas pelo irmão
louco e o segundo represente o número total de carneiros não roubados.

Exemplo de Entrada	Exemplo de Saída
8                        8 68
1 3 5 7 11 13 17 19

8                       7 63
1 3 5 7 11 13 16 19
'''
n = int(input())
nums = input()
nums = map(int, nums.split())
pos, soma, total = 0, 0, 0
continua = True

for i, num in enumerate(nums):
    total += num
    if(num % 2 == 0 and continua):
        ataques = i + 1
        soma += ((i * 2) + 1) - pos
        continua = False
    if(num - 1 == 0 and continua):
        pos = i + 1
else:
    if(soma > 0):
        total -= soma
    else:
        ataques = n
        total -= ataques
print(f'{ataques} {total}')
