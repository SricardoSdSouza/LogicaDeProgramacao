'''
Leia quatro números (N1, N2, N3, N4), cada um deles com uma casa decimal, correspondente às quatro notas de um aluno.
Calcule a média com pesos 2, 3, 4 e 1, respectivamente, para cada uma destas notas e mostre esta média acompanhada
pela mensagem "Media: ". Se esta média for maior ou igual a 7.0, imprima a mensagem "Aluno aprovado.".
Se a média calculada for inferior a 5.0, imprima a mensagem "Aluno reprovado.". Se a média calculada for um
valor entre 5.0 e 6.9, inclusive estas, o programa deve imprimir a mensagem "Aluno em exame.".
No caso do aluno estar em exame, leia um valor correspondente à nota do exame obtida pelo aluno.
Imprima então a mensagem "Nota do exame: " acompanhada pela nota digitada. Recalcule a média
(some a pontuação do exame com a média anteriormente calculada e divida por 2). e imprima a mensagem "Aluno aprovado."
(caso a média final seja 5.0 ou mais ) ou "Aluno reprovado.", (caso a média tenha ficado 4.9 ou menos).
Para estes dois casos (aprovado ou reprovado após ter pego exame) apresente na última linha uma mensagem "Media final:
" seguido da média final para esse aluno.
Entrada
A entrada contém quatro números de ponto flutuante correspendentes as notas dos alunos.
Saída
Todas as respostas devem ser apresentadas com uma casa decimal. As mensagens devem ser impressas conforme a
descrição do problema. Não esqueça de imprimir o enter após o final de cada linha, caso contrário obterá
"Presentation Error".
Exemplo de Entrada	Exemplo de Saída
2.0 4.0 7.5 8.0          Media: 5.4
6.4                      Aluno em exame.
                         Nota do exame: 6.4
                         Aluno aprovado.
                         Media final: 5.9

2.0 6.5 4.0 9.0          Media: 4.8
                         Aluno reprovado.

9.0 4.0 8.5 9.0          Media: 7.3
                         Aluno aprovado.
'''
numero = input('Informe as 4 notas do aluno: ').split()
n1 = float(numero[0])*2
n2 = float(numero[1])*3
n3 = float(numero[2])*4
n4 = float(numero[3])*1
media = (n1 + n2 + n3 +n4)/10

if media >= 7.0:
    print(f'Media: {media:.1f}')
    print('Aluno aprovado')
elif media < 5.0:
    print(f'Media: {media:.1f}')

    print('Aluno reprovado')
if media >= 5.0 and media < 7.0:
    print(f'Media: {media:.1f}')
    print('Aluno em exame.')
    nota_exame = float(input('Informe a nota do exame: '))
    print(f'Nota do exame: {nota_exame:.1f}')
    if ((nota_exame + media)/2) > 5.0:
        print('Aluno aprovado')
        print(f'Media final : {(nota_exame + media)/2:.1f}')

