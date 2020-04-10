import random
import logging
logging.disable(logging.CRITICAL)  # uncomment to disable logging messages
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s- %(levelname)s- %(message)s')
logging.basicConfig(level=logging.CRITICAL,
                    format='%(asctime)s- %(levelname)s- %(message)s')
logging.debug('Start of program')

coin = ['heads', 'tails']
guess = ''
while guess not in coin:
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    logging.debug('Guess entered is (%s)' % guess)
toss = coin[random.randint(0, 1)]  # 0 is tails, 1 is heads
logging.debug('Toss is (%s)' % toss)
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
