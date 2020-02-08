
def commaCode(commaList):
    commaReturn = ''
    if commaList == []:
        commaReturn = 'No items in list to process.'
    if len(commaList) == 1:
        commaReturn = commaList[0]
        return commaReturn
    for item in range(len(commaList)):
        if item == len(commaList) - 2:
            sep = ', and '
        elif item == len(commaList) - 1:
            sep = ''
        else:
            sep = ', '
        commaReturn = commaReturn + commaList[item] + sep


    return commaReturn

# spam = []
# spam = ['test']
# spam = ['apples', 'bananas', 'tofu', 'cats']
spam = ['dog', 'cat', 'rabbit', 'goldfish', 'lemur']
print(commaCode(spam))
