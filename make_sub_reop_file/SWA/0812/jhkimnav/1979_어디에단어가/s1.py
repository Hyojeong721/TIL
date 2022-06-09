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
    arr = [[0] * N for i in range(N)]

    # N * N의 배열에 퍼즐의 모양 정보 입력받기
    # 흰색 부분은 1, 검은색 부분은 0
    for n in range(N):
        arr[n] = list(map(int, input().split()))

    for i in range(N):
        for j in range(N):
            is_answer = True
            # 퍼즐의 셀이 검은색 부분이면 다음 셀로 이동
            if arr[i][j] == 0:
                continue
            if j != 0:
                # 이전 셀이 흰색이라면 다음 셀로이동
                if arr[i][j-1] == 1:
                    continue
            # 오른쪽 검사
            ni = i
            nj = j
            for k in range(K-1):
                ni = ni + 0
                nj = nj + 1
                if nj >= N:
                    is_answer = False
                elif arr[ni][nj] == 0:
                    is_answer = False
            if is_answer == True:
                if nj+1 >= N or arr[ni][nj+1] == 0:
                    answer += 1

    for i in range(N):
        for j in range(N):
            is_answer = True
            # 퍼즐의 셀이 검은색 부분이면 다음 셀로 이동
            if arr[i][j] == 0:
                continue
            if i != 0:
                if arr[i-1][j] == 1:
                    continue
            # 아래 검사
            is_answer = True
            ni = i
            nj = j
            for k in range(K-1):
                ni = ni + 1
                nj = nj + 0
                if ni >= N:
                    is_answer = False
                elif arr[ni][nj] == 0:
                    is_answer = False
            if is_answer == True:
                if ni+1 >= N or arr[ni+1][nj] == 0:
                    answer += 1

    print('#{} {}'.format(test_case, answer))



