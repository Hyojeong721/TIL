integers = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
n = len(integers)

for i in range(1 << n):
    temp = []
    for j in range(n):
        if i & (1 << j):
            temp.append(integers[j])
    if not sum(temp):
        print(temp)