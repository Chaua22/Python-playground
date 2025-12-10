from time import sleep
ficha = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) /2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? S/N: '))
    if resp in 'Nn':
        break
print('-='*30)
print(f'{"No.":<4}{"Nome":<10}{"Media":>8}')
print('-'*26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*30)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe)'))
    if opc == 999:
        sleep(1)
        print('-'*10, 'Finalizando', '-'*10)
        break
    if opc <= len(ficha):
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
sleep(1)
print('<<<<VOLTE SEMPRE>>>>')
