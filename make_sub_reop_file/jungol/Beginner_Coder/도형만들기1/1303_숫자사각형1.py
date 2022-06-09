# 높이n 너비m
n, m = map(int, input().split())
cnt = 1

for i in range(n):
    for j in range(m):
        print(cnt, end=' ')
        cnt += 1
    print()