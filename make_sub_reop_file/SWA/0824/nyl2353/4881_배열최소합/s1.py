'''

Pass

이게 백트래킹인지는 잘 모르겠지만 s2보다 효율적으로 짰다.

'''
import sys
sys.stdin = open('input.txt')

def find_minsum(mat, N, row, temp_sum):
    """
    N차 정사각행렬의 최소 합을 찾는 함수

    :param mat: 찾을 행렬 (N*N)
    :param N: 행렬의 길이
    :param row: 채우기 시작할 행의 인덱스
    :param temp_sum: 이전 행까지의 누적 합
    :return: X
    """
    global min_sum

    # 모든 열을 탐색
    for i in range(N):
        # 해당 열이 사용 전이면, 체크하고 누적 합에 추가
        if not check_col[i]:
            check_col[i] = 1
            temp_sum += mat[row][i]

            # 지금까지의 합이 최소 합 이상이면, 체크 취소하고 다음 열 검사
            if temp_sum >= min_sum:
                check_col[i] = 0
                temp_sum -= mat[row][i]
                continue

            # 지금까지의 합이 최소 합 미만이면,
            else:
                # 모든 열을 검사했을 경우, min_sum 업데이트
                if row == N-1:
                    min_sum = temp_sum
                # 검사할 열이 남았으면, 다음 열부터 검사 시작
                else:
                    find_minsum(mat, N, row + 1, temp_sum)

            # 다음 열도 탐색하기 위해 값 돌려놓음
            check_col[i] = 0
            temp_sum -= mat[row][i]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]

    min_sum = N * 10            # 최소 합의 가능한 가장 큰 값 (배열의 각 항목은 10 이하)
    check_col = [0] * N         # 각 열의 인덱스가 사용중인지 나타내는 배열
    find_minsum(mat, N, 0, 0)   # 0번째 행부터 시작
    print('#{} {}'.format(tc, min_sum))
