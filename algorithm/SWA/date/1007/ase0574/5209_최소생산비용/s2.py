# pass
import sys
sys.stdin = open('input.txt')

def bfs(cnt, ans):
    global min_ans, start
    # 첫 완성품일 경우
    if start == 0:
        if cnt == N:
            start = 1
            min_ans = ans

    # min_ans 정해진 이후의 경우
    else:
        # 빽트레킹/지금 과정결과가 min_ans보다 작으면 다음과정은 하지도말어~
        if min_ans <= ans:
            return

        else:
            if cnt == N:
                min_ans = ans
                return


    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            new_ans = ans + arr[cnt][i]
            bfs(cnt+1, new_ans)
            visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    min_ans = 0
    start = 0

    bfs(0, 0)

    print("#{} {}".format(tc, min_ans))