import random
game=['rock','paper','scissors']
player1=input('enter your choice as player1 ')
player2=random.choice(game)
print('player1 choice is',player1)
print('player2 choice is',player2)
print('result is')
if((player1=='rock')and(player2=='paper')):
    print('player2 wins')
elif((player1=='rock')and(player2=='scissors')):
    print('player1 wins')
elif((player1=='paper')and(player2=='rock')):
    print('player1 wins')
elif((player1=='paper')and(player2=='scissors')):
    print('player2 wins')
elif((player1=='scissors')and(player2=='rock')):
    print('player2 wins')
elif((player1=='scissors')and(player2=='paper')):
    print('player1 wins')
else:
    print('tie')

