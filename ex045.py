#Rock Paper Scissors 
import random
user = str(input('Escolha entre r = rock, p = paper e s = scissors: ')).strip()
lista_escolhas = ['r', 'p', 's']
pc = random.choice(lista_escolhas)
print(f'Você joga {user}')
print(f'Eu jogo {pc}')
if user == pc:
    print('Empate!')
elif user == 'r' and pc == 's' or user == 'p' and pc == 'r' or user == 's' and pc == 'p':
    print('Você venceu!')
elif user != 'r' or user != 's' or user != 'p':
    print('Jogada inválida!')
else:
    print('Eu venci!')
