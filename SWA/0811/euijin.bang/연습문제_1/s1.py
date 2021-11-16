import sys
sys.stdin = open("input.txt")

'''
문제
1. 5 X 5 2차 배열에 무작위로 25개의 숫자 초기화
2. 25개의 각 요소에 대해 그 요소와 이웃한 요소와의 차의 절대값을 구하시오.
3. 25개 요소에 대해 모두 조사하여 총합을 구하시오.
단, 벽에 있는 요소는 이웃 요소가 없을 수 있다. ([0][0]에 이웃한 요소 2개이다.)
'''


def getABS(a, b):
    """
    인자로 들어온 두 정수 차이의 절대값을 반환하는 함수
    :param a: var 1 (int)
    :param b: var 2 (int)
    :return: abs(a-b)
    """
    if a >= b:
        return a - b
    else:
        return -(a - b)


T = int(input())

for tc in range(1, T+1):
    # N : 구하려는 배열의 가로&세로 길이
    N = int(input())

    # arr : 이차원 리스트 초기화
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 델타 검색 (벽 부분 주의)
    del_i = [0, 1, 0, -1]
    del_j = [1, 0, -1, 0]

    # 구한 절대값의 총합 구하기
    total_ABS = 0

    for i in range(N):
        for j in range(N):
            for k in range(4):
                if (i + del_i[k] >= 0 and i + del_i[k] < N) and (j + del_j[k] >= 0 and j + del_j[k] < N):
                    #(arr[i + del_i[k]][j + del_j[k]])

    # 해당 요소와 이웃 요소의 절대값 구하기
                    target = arr[i][j]
                    target_del = arr[i + del_i[k]][j + del_j[k]]
                    total_ABS += getABS(target, target_del)

    print("#{} {}".format(tc, total_ABS))