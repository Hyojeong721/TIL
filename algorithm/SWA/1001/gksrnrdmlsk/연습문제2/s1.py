runs = []
for i in range(8):
    runs.append([i, i+1, i+2])

gins = []

for i in range(10):
    for j in range(10):
        gins.append(sorted([i] * 3 + [j] * 3))

for i in range(10):
    temp2 = [i, i, i]
    for j in range(8):
        temp = temp2 + runs[j]
        temp.sort()
        gins.append(temp)

for x in range(8):
    for y in range(8):
        temp = runs[x] + runs[y]
        temp.sort()
        gins.append(temp)

def is_gins(number):
    lst = list(map(int, number))
    lst.sort()
    if lst in gins:
        return True
    else:
        return False

values = ['124783', '667767', '054060', '101123']

for value in values:
    print(is_gins(value))

print(gins)
