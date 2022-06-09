n, m = map(int, input().split())

if n % 2 == 1 and 0 < n < 100 and 1 <= m <= 3:
    if m == 1:
        cnt = 1
        for i in range(1, n+1):
            if i % 2: #홀수
                for j in range(i):
                    print(cnt, end=' ')
                    cnt += 1

            else:
                ans = cnt + i -1
                cnt = ans + 1
                for j in range(i):
                    print(ans, end=' ')
                    ans -= 1
            print()

    elif m == 2:
        cnt = 0
        pad = 0
        for i in range(n-1, -1, -1):
            print(' '*pad, end='')
            for j in range(2*i+1):
                print(cnt, end=' ')
            print()
            pad += 2
            cnt += 1

    elif m == 3:
        cnt = 1
        for i in range(n//2+1):
            cnt = 1
            for j in range(i+1):
                print(cnt, end=' ')
                cnt += 1
            print()

        for i in range(n//2, 0, -1):
            cnt = 1
            for j in range(i):
                print(cnt, end=' ')
                cnt += 1
            print()

else:
    print("INPUT ERROR!")