# 패딩을 우측과 하단에 까만색(0)으로 패딩을 줌

import sys
sys.stdin = open('input.txt')

T = int(input())

# 방향 : 우하
dx = [1, 0]
dy = [0, 1]

for test_case in range(1, T+1):
    answer = 0
    # N : 단어 퍼즐의 가로, 세로 길이 N * N
    # K : 단어의 길이
    N, K = list(map(int, input().split()))
    arr = [[0] * (N+1) for i in range(N+1)]

    # N * N의 배열에 퍼즐의 모양 정보 입력받기
    # 흰색 부분은 1, 검은색 부분은 0
    for n in range(N):
        arr[n] = list(map(int, input().split()))
        arr[n].append(0)

    # for n in range(N+1):
    #     #     print(arr[n])
    #     # print()

    for i in range(N+1):
        cnt = 0
        for j in range(N+1):
            if arr[i][j] == 1:
                cnt += 1
            else:
                if cnt == K:
                    answer += 1
                cnt = 0

    for j in range(N+1):
        cnt = 0
        for i in range(N+1):
            if arr[i][j] == 1:
                cnt += 1
            else:
                if cnt == K:
                    answer += 1
                cnt = 0

    print('#{} {}'.format(test_case, answer))