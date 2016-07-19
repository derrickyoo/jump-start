import random

print('--------------------------------------------')
print('           GUESS THAT NUMBER GAME           ')
print('--------------------------------------------')
print()

the_num = random.randint(0, 100)
guess_num = -1

while guess_num != the_num:
    guess_str = input('Guess a number between a 0 and 100: ')
    guess_num = int(guess_str)

    if guess_num < the_num:
        print('Sorry but {} is LOWER than the number'.format(guess_num))
    elif guess_num > the_num:
        print('Sorry but {} is HIGHER than the number'.format(guess_num))
    else:
        print('YES! You\'ve got it. The number was {}'.format(guess_num))
