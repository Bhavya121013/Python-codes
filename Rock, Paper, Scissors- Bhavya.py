print('rock, paper, scissors')
print()
up=0
cp=0
import random
choices=['rock', 'paper', 'scissors']
x=int(input('enter the target points'))
while (True):
    uc=input('rock, paper, or scissors?')
    uc= uc.casefold()
    if uc in choices:
        pass
    else:
        print('your input is invalid')
        continue
    cc=random.choice(choices)
    if uc==cc:
        print('u have chosen',uc, 'and the computer has chosen', cc)
        print('it is a tie')
    elif uc=='paper' and cc=='rock':
        up+=1
        print('u have chosen',uc, 'and the computer has chosen', cc)       
        print('you got a point')
    elif uc=='rock' and cc=='scissors':
        up+=1
        print('u have chosen',uc, 'and the computer has chosen', cc)       
        print('you got a point')        
    elif uc=='scissors' and cc=='paper':
        up+=1
        print('u have chosen',uc, 'and the computer has chosen', cc)       
        print('you got a point')       
    else:
        cp+=1
        print('u have chosen',uc, 'and the computer has chosen', cc)       
        print('the computer got a point')
    print(f"the computer's  score is {cp}")
    print(f'your score is {up}')
    if up==x:
        break
    elif cp==x:
        break
    else:
        pass
if up==cp:
    print('It is a tie!')
elif up>cp:
    print('You win!')    
else:
    print('The computer wins!')
    print('Nice try')
print('Good game and I hope you enjoyed it')
