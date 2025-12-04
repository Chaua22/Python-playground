import random
opcoes = ['pedra', 'papel', 'tesoura']
print('=====JOKENPO=====')
print('Escolha uma opção: Pedra, papel ou tesoura.')

while True:
    usuario = str(input('Sua escolha: ').strip().lower())

    if usuario in opcoes:
        break
    else:print('Opção invalida! Tente novamente ')

computador = random.choice(opcoes)

print(f'Voce escolheu: {usuario}')
print(f'O computador escolheu {computador}')

if usuario == computador:
    print('Empate!')

elif(
    (usuario == 'pedra' and computador == 'tesoura') or
    (usuario == 'papel' and computador == 'pedra') or
    (usuario == 'tesoura' and computador == 'papel')
):
    print('Voce venceu!')
else:
    print('Voce perdeu.')
