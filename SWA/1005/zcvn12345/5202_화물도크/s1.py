import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    req = []
    for _ in range(N):
        req.append(list(map(int, input().split())))
    req.sort(key=lambda x: x[1])
    cnt = 0
    now = 0
    for i in req:
        if i[0] >= now:
            cnt += 1
            now = i[1]
    print(f'#{tc} {cnt}')
