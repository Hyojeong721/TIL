N = [-1, 3, -9, 6, 7, -6, 1, 5, 5, -2]
n = len(N)
total = []
for i in range(1<<n):
    temp = []
    zero = 0
    for j in range(n):
        if i & (1 << j):
            temp.append(str(N[j]))
            zero += N[j]
        if zero == 0 and temp != []:
            if temp not in total:
                total.append(temp[:])

print(total)
