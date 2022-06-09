import sys
sys.stdin = open('input.txt')

T = int(input())


def permutation(k, cursum):
    global visited, result

    # 가지치기 : 현재 합이 result보다 크다면 더이상 더할 가치가 없음
    if result <= cursum:
        return

    # 전체를 다 바꾼경우 => 순열이 하나 생성
    if k == N:
        if result > cursum:
            result = cursum
    else:
        for idx in range(k, N):
            visited[k], visited[idx] = visited[idx], visited[k]
            permutation(k+1, cursum + arr[k][visited[k]])
            visited[k], visited[idx] = visited[idx], visited[k]


for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    stack = []
    result = 987654321
    for i in range(N):
        visited[i] = i

    for i in range(N):
        min_arr = 9
        for j in range(N):
            if j in stack:
                pass
            elif min_arr > arr[i][j]:
                min_arr = arr[i][j]
                a = j
        stack.append(a)
        result += min_arr

    permutation(0, 0)

    print(result)

