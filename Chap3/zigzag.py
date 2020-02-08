"""
Zigzag game
Shows a simple zigzag animation
Press Ctrl-C to stop the program.
"""

import time

starLength = 8
delay = 0.04
fullIndent = 30
indentSize = 0
indentChar = '~'

for i in range(2):  # The main program loop
    # Zig to the right 20 times.
    for indentSize in range(fullIndent):
        time.sleep(delay)
        print(indentChar * indentSize + '*' * starLength)


    # Zag to the left 20 times.
    for indentSize in range(fullIndent, 0, -1):
        time.sleep(delay)
        print(indentChar * indentSize + '*' * starLength)
