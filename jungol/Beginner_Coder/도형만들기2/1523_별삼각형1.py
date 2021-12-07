n, m = map(int, input().split())

if 0 < n <= 100 and 1 <= m <= 3:
    if m == 1:
        cnt = 1
        for i in range(1, n+1):
            print('*'*i)
    elif m == 2:
        cnt = 1
        for i in range(n, -1, -1):
            print('*'*i)
    elif m == 3:
        for i in range(n):
            cnt = 2*i+1
            ans = '*'*cnt
            print(ans.center(2*n))
else:
    print("INPUT ERROR!")