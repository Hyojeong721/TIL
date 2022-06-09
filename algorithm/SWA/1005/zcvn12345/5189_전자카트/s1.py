import sys
sys.stdin = open('input.txt')

T = int(input())

def search(start, total, visited):
    global min_total, N
    if len(visited) == N:
        total += mat[start][0]
        if total < min_total:
            min_total = total
    else:
        for i in range(N):
            if i != start and i not in visited:
                # new_total = total + mat[start][i]
                # new_visited = visited + [i]
                # total += mat[start][i]
                # visited.append(i)
                search(i, total+mat[start][i], visited + [i])


for tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    min_total = 1000000000
    search(0, 0, [0])
    print(f'#{tc} {min_total}')