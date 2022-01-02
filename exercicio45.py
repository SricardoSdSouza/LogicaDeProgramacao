''' 45 - Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno
# a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota
# (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai
# utilizar o sistema. Após todos os alunos terem respondido informar:
#   1 - Maior e Menor acerto;
#   2 - Total de Alunos que utilizaram o sistema;
#   3 - A Média das Notas da Turma.
#    Gabarito
#    01 - A
#    02 - B
#    03 - C
#    04 - D
#    05 - E
#    06 - E
#    07 - D
#    08 - C
#    09 - B
#    10 - A
# Apos concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes dos alunos
# usarem o programa.'''
gabarito = []
respostas_aluno = []
notas_tiradas = []
print("\nProfessor: ")
for i in range(10):
    print('Questão:', i + 1)
    resposta_certa = gabarito.append(input('Informe a alternativa correta: ').upper())

n_aluno = 1
continuar = True
while continuar != 'N':
    print("Aluno nº", n_aluno, ":")
    respostas_aluno.clear()
    print(" As alternativas são : A, B, C, D. ")
    for i in range(10):
        print("Questão: ", i + 1)
        r = input("Escolha a alternativa: ").upper()
       # respostas_aluno.append(input("Escolha a alternativa: ").upper())
        while not r in ('A', 'B', 'C', 'D'):
            print('Escolha dentre as alternativas (A, B, C, D.): ')
            r = input("Escolha a alternativa: ").upper()
        respostas_aluno.append(r)
        resposta_aluno = respostas_aluno

    nota = 0
    for i in range(10):
        if respostas_aluno[i] == gabarito[i]:
            nota += 1
    notas_tiradas.append(nota)
    # outro = input("Outro aluno vai utilizar o sistema? [s/n] : ").upper()
    continuar = input("Outro aluno vai utilizar o sistema? [s/n] : ").upper()
    while not continuar in ('S','N'):
        print('Digite N para terminar ou S para outro aluno. !')
        continuar = input("Outro aluno vai utilizar o sistema? [s/n] : ").upper()

    n_aluno += 1

print(len(notas_tiradas), "alunos utilizaram o sistema")
print("\nA maior nota tirada foi: ", max(notas_tiradas))
print("A menor nota tirada foi: ", min(notas_tiradas))
print("A media de notas da turma foi de:", sum(notas_tiradas) / len(notas_tiradas))
print(notas_tiradas)