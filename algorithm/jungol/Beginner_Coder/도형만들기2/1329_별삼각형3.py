n = int(input())

if n % 2 == 1 and 0 < n < 100:
    mid = n//2 + 1
    for i in range(mid):
        padding = ' ' * i
        cnt = 2*i+1
        ans = '*' * cnt
        print(padding, end='')
        print(ans)

    for i in range(mid-2, -1, -1):
        padding = ' ' * i
        cnt = 2*i+1
        ans = '*' * cnt
        print(padding, end='')
        print(ans)
else:
    print("INPUT ERROR!")