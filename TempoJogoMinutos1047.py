'''
Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo.
Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.
Entrada
Quatro números inteiros representando a hora de início e fim do jogo.
Saída
Mostre a seguinte mensagem: “O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)” .
Exemplo de Entrada	Exemplo de Saída
7 8 9 10      O JOGO DUROU 2 HORA(S) E 2 MINUTO(S)

7 7 7 7       O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)

7 10 8 9      O JOGO DUROU 0 HORA(S) E 59 MINUTO(S)
'''
hora_entrada = input().split()

hora_inicial = int(hora_entrada[0])
minuto_inicial = int(hora_entrada[1])
hora_final = int(hora_entrada[2])
minuto_final = int(hora_entrada[3])

if hora_inicial < hora_final:
    h = hora_final - hora_inicial
    if minuto_inicial < minuto_final:
        m = minuto_final - minuto_inicial
    if minuto_inicial > minuto_final:
        h = h-1
        m = (60 - minuto_inicial) + minuto_final
    if minuto_inicial == minuto_final:
        m = 0
if hora_inicial > hora_final:
    h = (24 - hora_inicial) + hora_final
    if minuto_inicial < minuto_final:
        m = minuto_final - minuto_inicial
    if minuto_inicial > minuto_final:
        h = h - 1
        m = (60 - minuto_inicial) + minuto_final
    if minuto_inicial == minuto_final:
        m = 0
if hora_inicial == hora_final:
    if minuto_inicial < minuto_final:
        m = minuto_final - minuto_inicial
        h = 0
    if minuto_inicial > minuto_final:
        m = (60 - minuto_inicial) + minuto_final
        h = 23
    if minuto_inicial == minuto_final:
        h = 24
        m = 0

print(f'O JOGO DUROU {h} HORA(S) E {m} MINUTO(s)')
''' Ou desta forma'''
x = input().split()
hi, mi, hf, mf = x

hi = int(x[0])
mi = int(x[1])
hf = int(x[2])
mf = int(x[3])

if hi < hf:
    h = hf - hi
    if mi < mf:
        m = mf - mi
    if mi > mf:
        h = h - 1
        m = (60 - mi) + mf
    if mi == mf:
        m = 0
if hi > hf:
    h = (24 - hi) + hf
    if mi < mf:
        m = mf - mi
    if mi > mf:
        h = h - 1
        m = (60 - mi) + mf
    if mi == mf:
        m = 0
if hi == hf:
    if mi < mf:
        m = mf - mi
        h = 0
    if mi > mf:
        m = (60 - mi) + mf
        h = 23
    if mi == mf:
        h = 24
        m = 0

print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(h, m))