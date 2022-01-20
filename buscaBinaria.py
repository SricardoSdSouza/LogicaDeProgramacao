'''BUSCA BINÁRIA'''

def busca(lista,x):
    primeiro = 0
    ultimo = len(lista)-1

    while primeiro <= ultimo:
        meio = (primeiro + ultimo)//2
        if lista[meio] == x:
           # print(meio)
            return meio
        elif x < lista[meio]:
            ultimo = meio - 1
        else:
            primeiro = meio + 1
       # print(meio)

    return False
lista = [12, 13, 14, 15, 16, 17, 21, 22, 34, 54, 67]
print(busca(lista, 34))
