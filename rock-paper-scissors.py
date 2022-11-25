#Rock Paper Scissors 
import random
user = str(input('Choose between r = rock, p = paper e s = scissors: ')).strip()
list_choices = ['r', 'p', 's']
pc = random.choice(list_choices)
print(f'U chose {user}')
print(f'I chose {pc}')
if user == pc:
    print('Tie!')
elif user == 'r' and pc == 's' or user == 'p' and pc == 'r' or user == 's' and pc == 'p':
    print('U won!')
elif user != 'r' or user != 's' or user != 'p':
    print('Invalid choice!')
else:
    print('I won!')
