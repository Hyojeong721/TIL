import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    # N : 배열의 크기
    # M : 파리채의 크기
    N, M= list(map(int, input().split()))
    arr = [[0] * N for i in range(N)]
    max_kill = 0

    # N * N의 배열에 파리의 갯수 입력받기
    for n in range(N):
        arr[n] = list(map(int, input().split()))

    for i in range(N):
        for j in range(N):
            sum_kill = 0
            for k in range(i, i+M):
                for l in range(j, j+M):
                    if 0 <= k < N and 0 <= l < N:
                        sum_kill += arr[k][l]

            if sum_kill > max_kill:
                max_kill = sum_kill

    print('#{} {}'.format(test_case, max_kill))