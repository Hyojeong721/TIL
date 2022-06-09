m = int(input())
n = int(input())
res = []

for num in range(m, n+1):
    arr = []
    sqrt = int(num**(1/2))
    for i in range(1, sqrt+1):
        if num % i == 0:
            arr.append(i)
            if num / i != i:
                arr.append(int(num/i))

        if len(arr) > 2:
            break
    if len(arr) == 2:
        res.append(num)

if len(res):
    res.sort()
    sum = 0
    for s in res:
        sum += s
    print(sum)
    print(res[0])
else:
    print(-1)