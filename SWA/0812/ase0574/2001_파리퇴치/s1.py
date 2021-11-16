# 0827
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # N은 검색할 판 사이즈 / M은 파리채 사이즈
    N, M = list(map(int,input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    # 탐색할 자리 (0,0) ~ (i,j)
    for i in range(N-M+1):
        for j in range(N-M+1):
            die = 0
            # 파리 채 사이즈만큼 탐색
            for row in range(M):
                for col in range(M):
                    die += arr[i+row][j+col]

            # 제일 큰값만 저장하기
            if result < die:
                result = die

    print("#{} {}".format(tc, result))