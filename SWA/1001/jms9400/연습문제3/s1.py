# 부분집합 합 문제 구현 (모든 원소 합 0이 되는 부분집합 출력)

lst = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]

n = len(lst)

# 바이너리 카운팅
for i in range(1, 1<<n):
    temp = []
    for j in range(n):
        if i & (1<<j):
            temp.append(lst[j])
    if sum(temp) == 0:
        print(temp)


# 순열(순서o) 조합(순서x)  -> 조합 활용!

def comb(n, r):
    if r == 0:
        if sum(tr) == 0:
            print(tr)
    elif n < r:
        return
    else:
        tr[r-1] = lst[n-1]
        comb(n-1, r-1)
        comb(n-1, r)


for i in range(1, n):
    tr = [0] * i
    comb(n, i)
