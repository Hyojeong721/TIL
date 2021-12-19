def fibo(d, k):
    for j in range(k-1, 0, -1):
        cashe = [-1 for _ in range(d + 1)]
        cashe[d] = k
        cashe[d-1] = j
        for i in range(d-2, -1, -1):
            if cashe[i+2] < 0 or cashe[i+1] < 0:
                break
            if cashe[i+2] > cashe[i+1]:
                cashe[i] = cashe[i+2] - cashe[i+1]
                if cashe[1] != -1 and cashe[2] > cashe[1]:
                    return cashe[1], cashe[2]

    return '실패'

d, k = map(int, input().split())
a, b = fibo(d, k)
print(a)
print(b)

