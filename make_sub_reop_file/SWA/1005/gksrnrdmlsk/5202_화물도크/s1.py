import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = []
    for _ in range(N):
        lst.append(list(map(int, input().split())))
    lst.sort(key=lambda x: x[1])
    curr = lst[0][1]
    search = 1
    cnt = 1
    while search < N:
        if lst[search][0] >= curr:
            curr = lst[search][1]
            cnt += 1
        search += 1
    print('#{} {}'.format(tc, cnt))
