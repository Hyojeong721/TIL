import sys
sys.stdin = open('input.txt')


def backtracking(i, cnt): # i: 정류장 번호, cnt: 충전횟수
    global minimum
    if cnt > minimum:
        return

    if i >= N:     # 2  (5)  7  10:   7
        if cnt < minimum:
            minimum = cnt
    else:
        reachable = []
        for j in range(1, info[i]+1):
            reachable.append(i+j)
        # 1 /2/ 3 4 5
        # 2 3 1 1
        # i = 1
        if N in reachable:
            if cnt < minimum:
                minimum = cnt
        for station in reachable:
            backtracking(station, cnt+1)


T = int(input())

for tc in range(1, T+1):
    info = list(map(int, input().split()))
    N = info[0]
    info = [0] + info[1:]
    minimum = N
    visited = [0]*N
    backtracking(1, 0)
    print(f'#{tc} {minimum}')