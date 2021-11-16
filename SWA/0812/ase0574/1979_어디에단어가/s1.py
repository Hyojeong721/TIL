# 해결 안된 코드
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1):
    # 퍼즐길이 = N / 단어길이 = K
    N, K = map(int, input().split())
    total_list = []
    for n in range(N):
        arr = list(map(int, input().split()))
        total_list.append(arr)

    for n in range(N):

        result_row = 0
        result_col = 0

        #행에서 가능한 자리 확인
        for i in range(N):
            for j in range(N):
                sum_row = 0
                # 연속 자리 확인
                for k in range(K):
                    if j + k < N:
                        sum_row += total_list[i][j + k]
    # 조건1-전체 크기 넘어가지 않는 인덱스/ 조건2-단어길이와 크기 같을 것/ 조건3-단어길이보다 길지 않을 것.
                        if j+k+1 < N and sum_row == K and total_list[i][j+k+1] == 0:
                            result_row += 1
                            sum_row = 0


                print(result_row)



