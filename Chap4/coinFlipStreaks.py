# Coin Flip Streaks Exercise
import random
numberOfStreaks = 0
for experimentNumber in range(10000):

    # Create lis of 100 heads or tails

    coinFlips = []
    for flips in range(100):
        flip = random.randint(0, 1)
        if flip == 0:
            coinFlips.append('H')
        else:
            coinFlips.append('T')

    # Check if there is a streak of 6 heads or tails in a row.

    streak = 0
    for flip in range(len(coinFlips) - 1):
        if coinFlips[flip] == coinFlips[flip + 1]:
            streak += 1
            if streak == 6:
                numberOfStreaks += 1
                streak = 0
        else:
            streak = 0

print('Average streaks per 100 flips: %s' % (numberOfStreaks / 10000))
