n, m = map(int, input().split())
cnt = 1

if m == 1:
    for i in range(n):
        for j in range(n):
            print(cnt, end=' ')
        print()
        cnt += 1


elif m == 2:
    for i in range(n):
        if i % 2:# 홀수행 거꾸로
            cnt = n
            for j in range(n):
                print(cnt, end=' ')
                cnt -= 1
            print()
        else:
            cnt = 1
            for j in range(n):
                print(cnt, end=" ")
                cnt += 1
            print()
            cnt = 1

elif m == 3:
    for i in range(n):
        for j in range(1, n+1):
            print(cnt*j, end=" ")
        print()
        cnt += 1


