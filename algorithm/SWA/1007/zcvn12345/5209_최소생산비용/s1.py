import sys
sys.stdin = open('input.txt')

T = int(input())

def pick(visited, i, total):
    global result
    if total >= result:
        return
    if i == N:
        if total <= result:
            result = total
            return
    else:
        for j in range(N):
            if j not in visited:
                pick(visited+[j], i+1, total+mat[i][j])



for tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    result = 1000000000000000
    pick([], 0, 0)
    print(f'#{tc} {result}')