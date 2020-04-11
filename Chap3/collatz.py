#! python3


def collatz(number):
    if number % 2 == 0:
        numRet = number // 2
    else:
        numRet = 3 * number + 1
    print(numRet)
    return numRet


print('Please input an integer.')
try:
    inputNum = int(input())
except Exception:
    print('Need an integer here...')
    exit()
while inputNum != 1:
    inputNum = collatz(inputNum)
