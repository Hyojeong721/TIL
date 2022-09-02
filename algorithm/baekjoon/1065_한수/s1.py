import sys
sys.stdin = open('input.txt')


N= int(input())

cnt = 0

if N < 10:
    print(N)
else:
    for i in range(10, N+1):
        res = True
        temp = list(map(int, str(i)))
        t = temp[1] - temp[0]
        for k in range(1, len(temp)):
            if t != temp[k] - temp[k - 1]:
                res = False
                break
        if res:
            cnt += 1

    print(cnt+9)