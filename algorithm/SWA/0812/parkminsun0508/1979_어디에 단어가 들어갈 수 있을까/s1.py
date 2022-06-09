# 1979 어디에 단어가 들어갈 수 있을까
import sys
sys.stdin = open("input.txt")

#테스트 케이스 받아오기
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    # 결과값 초기화
    result = 0
    # 낱말 배열 리스트
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 단어는 1에 해당하는 빈 자리에만 들어갈 수 있다.
    # 그러나 자리가 남으면 안되고 양 옆, 위 아래 0인 경우, 즉 검정 칸이여지만 단어가 입력될 수 있다.
    # 1이 연속으로 K인지 반복 for문으로 각각 가로, 세로를 확인한다.
    for i in range(N):
        check_row = 0
        check_col = 0
        for j in range(N):
            # 가로를 확인한다.
            if arr[i][j] == 1:
                check_row += 1
            if arr[i][j] == 0:
                if check_row == K:
                    result += 1
                check_row = 0
            # 세로를 확인한다.
            if arr[j][i] == 1:
                check_col += 1
            if arr[j][i] == 0:
                if check_col == K:
                    result += 1
                check_col = 0
            if j == N-1:
                if check_row == K:
                    result += 1
                if check_col == K:
                    result += 1
                check_row = 0
                check_col = 0
    print('#{} {}'.format(tc, result))

