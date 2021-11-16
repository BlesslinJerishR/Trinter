#! python3


data = [['apples', 'oranges', 'cherries', 'banana'],
        ['Alice', 'Bob', 'Carol', 'David'],
        ['dogs', 'cats', 'moose', 'goose']]


def trinter(table):
    # create a new list of 3 "0" values: one for each list in tableData
    cwidth = [0] * len(table)
    # search for the longest string in each list of tableData
    for y in range(len(table)):
        for x in table[y]:
            if cwidth[y] < len(x):
                cwidth[y] = len(x)

    # ROTOR
    for x in range(len(table[0])):
        for y in range(len(table)):
            print(table[y][x].rjust(cwidth[y]), end=' ')
        print()
        x += 1


trinter(data)
