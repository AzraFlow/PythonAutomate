

def printTable(listOfLists):
    colWidths = [0] * len(listOfLists)

    for line in listOfLists:
        max = 0
        for word in line:
            if len(word) > max:
                max = len(word)
        colWidths[listOfLists.index(line)] = max


    for j in range(len(listOfLists[0])):
        for i in range(len(listOfLists)):
            print(listOfLists[i][j].rjust(colWidths[i]), end='  ')
        print()


tableData = [['apples', 'oranges', 'cherries', 'bannana'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]

tableData2 = [['green beans', 'tomatoes', 'peas', 'sweet potatos'],
            ['Joe', 'Keanu', 'Michael', 'Bradley'],
            ['rhinos', 'elephants', 'hippos', 'aardvarks']]

printTable(tableData)
print()
printTable(tableData2)
