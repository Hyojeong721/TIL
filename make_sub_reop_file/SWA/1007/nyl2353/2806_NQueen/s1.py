'''
    [for ~ else 문]
        - for 문이 break 등으로 중간에 빠져나오지 않고 끝까지 실행됐을 경우, else 문 실행

'''
import sys
sys.stdin = open('input.txt')


def find_safe(r):
    global cnt, visited

    if r == N:
        cnt += 1
        return

    for c in range(N):
        # 열 검사
        if visited.get(c, -1) == -1:
            # 대각선 검사
            for dc in range(r+1):
                if c-dc >= 0 and visited.get(c-dc, -1) == r-dc:
                    break
                if c+dc < N and visited.get(c+dc, -1) == r-dc:
                    break
            # 검사 완
            else:
                visited[c] = r
                find_safe(r+1)
                visited[c] = -1

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cnt = 0
    visited = {}    # 방문한 {열: 행}
    find_safe(0)
    print('#{} {}'.format(tc, cnt))