print('SEQUÊNCIA DE FIBONACCI')
n = int(input('Informe o número para a sequência de Fibonacci: '))
primeiro = 0
segundo = 1
print(f'{primeiro} -> {segundo}',end="")
contador = 3
while contador <= n:
    sequencia = primeiro + segundo
    print(f' -> {sequencia}',end="")
    primeiro = segundo
    segundo = sequencia
    contador += 1
print(' -> FIM !! :)')

# usando o For
primeiro = 0
segundo = 1
soma = primeiro + segundo
n = int(input('Informe o número para a sequência de Fibonacci: '))
for i in range(0, n):
    soma = primeiro + segundo
    primeiro = segundo
    segundo = soma

print(primeiro)