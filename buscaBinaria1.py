lista = [12, 13, 14, 15, 16, 17, 21, 22, 34, 54, 67]
print('''
    A lista é composta dos seguintes Números:
    = 12, 13, 14, 15, 16, 17, 21, 22, 34, 54, 67
    ''')
numero = int(input('Informe o número que saber a posição: '))

primeiro = 0
ultimo = len(lista)-1
while primeiro <= ultimo:
    #faço a divisão da lista para encontrar o número mediano
    meio = (primeiro + ultimo)//2
    #  testo se o número mediano é igual ao numero informado
    if lista[meio] == numero:
        print(f'I número procurado esta na posição {meio}')
        break
    elif numero < lista[meio]:
        ultimo = meio - 1
    else:
        primeiro = meio + 1
