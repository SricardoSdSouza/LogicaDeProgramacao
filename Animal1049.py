'''
Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível segundo o esquema abaixo, da esquerda para a direita.  Em seguida conclua qual dos animais seguintes foi escolhido, através das três palavras fornecidas.

                carnivoro ---- aguia
            ave
                onivoro ----- pomba
vertebrado
                     onivoro ------homem
            mamifero
                     herbivoro ----vaca

                   hematofogo ---- pulga
            inseto
                   herbivoro ----- lagarta
invertebrado
                     hematofogo ------homem
            anelideo
                     onivoro ----minhoca

Entrada
A entrada contém 3 palavras, uma em cada linha, necessárias para identificar o animal segundo a figura acima, com todas as letras minúsculas.

Saída
Imprima o nome do animal correspondente à entrada fornecida.

Exemplos de Entrada      	Exemplos de Saída
vertebrado
mamifero                        homem
onivoro

vertebrado                      aguia
ave
carnivoro

invertebrado                   minhoca
anelideo
onivoro
'''
info1 = input().upper()
info2 = input().upper()
info3 = input().upper()

if info1 == 'VERTEBRADO'and info2 == 'MAMIFERO' and info3 == 'ONIVORO':
        print('homem')

if info1 == 'VERTEBRADO'and info2 == 'MAMIFERO' and info3 == 'HERBIVORO':
        print('vaca')

if info1 == 'VERTEBRADO'and info2 == 'AVE' and info3 == 'CARNIVORO':
        print('aguia')

if info1 == 'VERTEBRADO'and info2 == 'AVE' and info3 == 'ONIVORO':
        print('pomba')

if info1 == 'INVERTEBRADO'and info2 == 'INSETO' and info3 == 'HEMATOFAGO':
        print('pulga')

if info1 == 'INVERTEBRADO'and info2 == 'INSETO' and info3 == 'herbivoro':
        print('lagarta')

if info1 == 'INVERTEBRADO'and info2 == 'ANELIDEO' and info3 == 'HEMATOFAGO':
        print('sanguessuga')

if info1 == 'INVERTEBRADO'and info2 == 'ANELIDEO' and info3 == 'ONIVORO':
        print('minhoca')
