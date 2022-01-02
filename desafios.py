'''Leia 2 valores inteiros e armazene-os nas variáveis A e B. Efetue a soma de A e B atribuindo o seu resultado
na variável X. Imprima X conforme exemplo apresentado abaixo. Não apresente mensagem alguma além daquilo que está
sendo especificado e não esqueça de imprimir o fim de linha após o resultado, caso contrário, você receberá
"Presentation Error".
Entrada
A entrada contém 2 valores inteiros.
A = 10 e B = 9
Saída
Imprima a mensagem "X = " (letra X maiúscula) seguido pelo valor da variável X e pelo final de linha. Cuide para que
 um espaço antes e depois do sinal de igualdade, conforme o exemplo abaixo.
 X = 19 '''

A = int(input('informe um número: '))
B = int(input('informe um número: '))
x = A + B
print('X =', format(x))


'''
A fórmula para calcular a área de uma circunferência é: area = π . raio2. Considerando para este problema que π = 3.14159:
- Efetue o cálculo da área, elevando o valor de raio ao quadrado e multiplicando por π.
Entrada
A entrada contém um valor de ponto flutuante (dupla precisão), no caso, a variável raio.
Saída
Apresentar a mensagem "A=" seguido pelo valor da variável area, conforme exemplo abaixo, com 4 casas após o ponto decimal.
 Utilize variáveis de dupla precisão (double). Como todos os problemas, não esqueça de imprimir o fim de linha após o resultado,
caso contrário, você receberá "Presentation Error".'''

n = float(3.14159)
raio = float(100.64)
area = n*(raio*raio)

print(f'A={area:.4f}')

'''
Leia 2 valores de ponto flutuante de dupla precisão A e B, que correspondem a 2 notas de um aluno. 
A seguir, calcule a média do aluno, sabendo que a nota A tem peso 3.5 e a nota B tem peso 7.5 
(A soma dos pesos portanto é 11). Assuma que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.
Entrada
O arquivo de entrada contém 2 valores com uma casa decimal cada um.

Saída
Imprima a mensagem "MEDIA" e a média do aluno conforme exemplo abaixo, com 5 dígitos após o ponto decimal 
e com um espaço em branco antes e depois da igualdade. Utilize variáveis de dupla precisão (double) 
e como todos os problemas, não esqueça de imprimir o fim de linha após o resultado, caso contrário, 
você receberá "Presentation Error".'''

a = float(input())
b = float(input())
p1 = 3.5
p2 = 7.5

print(f'MEDIA = {((a*p1)+(b*p2))/(p1+p2):.5f}')

# usando 3 valores de entrada
A = float(input())
B = float(input())
C = float(input())
p1 = 2
p2 = 3
p3 = 5

soma = (A*p1)+(B*p2)+(C*p3)
peso = p1 + p2 + p3
#print(f'MEDIA = {soma/peso:.1f}')
print(f'MEDIA = {(((A*p1)+(B*p2)+(C*p3))/(p1 + p2 + p3)):.1f}')