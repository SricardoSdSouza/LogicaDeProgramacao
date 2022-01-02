for i in range(10):
    aluno = int(input(f'Digite um numero do {i+1}º aluno: '))
    altura = float(input(f'Digite a altura do {i+1}º aluno: '))
    if i == 0:
        mais_alto = aluno
        maior_altura = altura
    elif altura > maior_altura:
        mais_alto = aluno
        maior_altura = altura

print(f'O aluno mais alto é o número = {mais_alto} e tem {maior_altura}cm de altura.')