import sys
sys.stdin = open("input.txt")

def permutation(k, cursum):
    global visited, result

    # plunning 가지치지: 현재 값이 result 보다 크면 더 이상 더할 가치 없어서 함수를 끝낸다.
    if result <= cursum:
        return
    # result 조건
    # 전체를 다 바꾼 경우 => 순열이 하나 생성
    # 종료조건
    if k == N:
        # return '끝'
        # 모든 경우의 수의 합 => 시간초과 남 => result 보세욤
        if result > cursum:
            result = cursum
    else:
        for idx in range(k, N):
            visited[k], visited[idx] = visited[idx], visited[k]
            permutation(k+1, cursum + data[k][visited[k]]) # 한 뎁스씩 들어가면서 스왑, 원상복귀
            visited[k], visited[idx] = visited[idx], visited[k]

    # k 까지는 고정값이므로 더할 것
    pass

T = int(input())
for tc in range(1, T+1):
    N = int(input())

# 각 인덱스에서 하나만 뽑는다. 즉, 0, 1, 2, 3, 4 는 하나씩만 등장해야 하고
# 순열을 뽑고, 순열에 해당하는 데이터를 출력하면 된다.

    visited = [0] * N
    for i in range(N):
        visited [i] = i

    data = [list(map(int, input().split())) for _ in range(N)]

    result = 987654321

    permutation(0, 0) # 고정값 k 합산

    print(result)