# Repeat steps from part 1
file = open('inputs/day1.txt', 'r')
listLeft = []
listRight = []

for line in file:
    spacer = line.split()
    listLeft.append(int(spacer[0]))
    listRight.append(int(spacer[1]))

listRight.sort()
result = 0

for index, item in enumerate(listLeft):
    numleft = item
    maxValue = len(listRight)
    counter = 0
    duplicate = 0

    # Go through the whole list or while the left number is bigger than the right number
    while (counter < maxValue) and (numleft >= listRight[counter]):
        if numleft == listRight[counter]:
            duplicate = duplicate + 1
        counter += 1
    result = result + (numleft * duplicate)

print(result)
file.close()