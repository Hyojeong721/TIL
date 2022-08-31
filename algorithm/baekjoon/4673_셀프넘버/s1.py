N = 10000
main = [i for i in range(1, N)]
new = []

for i in main:
    temp = list(map(int, str(i)))
    res = i
    for t in temp:
        res += t
    new.append(res)

new = set(new)

for i in main:
    if i not in new:
        print(i)
