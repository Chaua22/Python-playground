from random import randint
from time import sleep
num = randint(1,60)
lista = []
jogos = []
cont = 0
print('-='*20)
print('           JOGA NA MEGACENA        ')
print('-='*20)
quant = int(input('Quantos jogos quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont+=1
        if cont >6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-'*11, f'Sorteando {quant} jogos', '-'*11)
for i, l in enumerate(jogos):
    sleep(1)
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-='*7, ' BOA SORTE ', '-='*7)
