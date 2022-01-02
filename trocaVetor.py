'''lista = [12, 13, 14, 15, 16, 17, 21, 22, 34, 54, 67]
lista1 = []
for i in range(len(lista)-1,-1,-1):
    lista1.append(lista[i])
print(lista1)'''

'''print('posição de um número em uma lista')
lista = [12, 13, 14, 15, 16, 17, 21, 22, 34, 54, 67]
for i in range(len(lista)):
    if lista[i] == 17:
        print(f'A posição do nº 17 é = {i}')'''
print('======================================================')
lista = [12, 13, 14, 15, 16, 17, 21, 22, 34, 54, 67,68]
aux = 0
j = -1
n = int(len(lista)//2)
for i in range(len(lista)-n):
    aux = lista[i]
    lista[i] = lista[j]
    lista[j] = aux
    #fim = lista[j]
    #lista.insert(i, fim)
    #lista.insert(j, aux)
    #lista.pop(j)
    j -= 1

print(lista)