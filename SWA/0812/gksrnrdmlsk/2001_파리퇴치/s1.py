import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = list(map(int, input().split()))
    lst = [list(map(int, input().split())) for _ in range(N)]
    total = 0
    for i in range(N - M + 1): # 좌상단을 기준으로 탐색합니다.
        for j in range(N - M + 1):
            temp = 0
            for x in range(M): # M*M 사각형 안의 원소의 합을 구합니다.
                for y in range(M):
                    temp += lst[i + x][j + y]
            if temp > total:
                total = temp # 최댓값을 업데이트합니다.

    print('#{} {}'.format(tc, total))
