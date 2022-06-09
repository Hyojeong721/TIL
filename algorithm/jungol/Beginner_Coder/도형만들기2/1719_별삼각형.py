n, m = map(int, input().split())

if 0 < n <= 100 and n%2 == 1 and 1 <= m <= 4:
    if m == 1:
        mid = n//2 + 1
        for i in range(1, mid+1):
            print('*'*i)
        for j in range(mid-1, -1, -1):
            print('*'*j)

    elif m == 2:
        mid = n//2 + 1
        for i in range(1, mid + 1):
            ans = '*' * i
            print(ans.rjust(mid))
        for j in range(mid - 1, -1, -1):
            ans = '*' * j
            print(ans.rjust(mid))

    elif m == 3:
        mid = n//2 + 1
        for i in range(mid-1, 0, -1):
            ans = '*' * (2*i+1)
            print(ans.center((2*n+1)//2))
        for i in range(mid):
            ans = '*' * (2*i+1)
            print(ans.center((2*n+1)//2))

    elif m == 4:
        mid = n // 2 + 1
        for i in range(mid, 0, -1):
            ans = '*' * i
            print(ans.rjust(mid))
        for j in range(2, mid+1):
            ans = '*' * j
            padding =' ' * (n//2)
            print(padding, end='')
            print(ans)
else:
    print("INPUT ERROR!")