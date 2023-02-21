# Jogo de pedra, papel e tesoura
import random
from time import sleep
lista = ['Pedra', 'Papel', 'Tesoura']
computador = random.choice(lista)
print('Suas opções:\n [ 0 ] Pedra\n [ 1 ] Papel\n [ 2 ] Tesoura')
escolha = int(input('Qual é a sua jogada? '))
print('\033[31mJO')
sleep(1)
print('\033[31mKEN')
sleep(1)
print('\033[31mPO!!!')
print('-=' * 15)
print('Computador jogou {}'.format(computador))
if escolha == 0:
    print('Jogador jogou Pedra')
elif escolha == 1:
    print('Jogador jogou Papel')
elif escolha == 2:
    print('Jogador jogou Tesoura')
print('-=' * 15)
if computador == 'Pedra':
    if escolha == 0:
        print('EMPATE')
    elif escolha == 1:
        print('JOGADOR VENCE')
    elif escolha == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 'Papel':
    if escolha == 0:
        print('COMPUTADOR VENCE')
    elif escolha == 1:
        print('EMPATE')
    elif escolha == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 'Tesoura':
    if escolha == 0:
        print('JOGADOR VENCE')
    elif escolha == 1:
        print('COMPUTADOR VENCE')
    elif escolha == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')









