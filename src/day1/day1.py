
# Open file and create lists
file = open('inputs/day1.txt', 'r')
listLeft = []
listRight = []

# Retrieve numbers from text file and add to lists
for line in file:
    spacer = line.split()
    listLeft.append(int(spacer[0]))
    listRight.append(int(spacer[1]))

# Sort the lists 
listLeft.sort()
listRight.sort()
result = 0

for index, item in enumerate(listLeft):
    numLeft = item
    numRight = listRight[index]
    result = result + (abs(numLeft - numRight))

print(result)
file.close()