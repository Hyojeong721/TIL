# 참조
# 조합으로 구현
arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]

n = len(arr)

def comb(n, r):
    if r == 0:
        if sum(tr) == 0:
            print(tr)
    elif n < r:
        return
    else:
        tr[r-1] = arr[n-1]
        comb(n-1, r-1)
        comb(n-1, r)


for i in range(1, n):
    tr = [0] * i
    comb(n, i)
