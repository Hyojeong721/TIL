'''

Fail (제한시간 초과)

가지치기 없이 전부 검사해서 제한시간 초과인 것 같다.
백트래킹으로 바꾸기보단 새로운 코드를 작성하는게 좋을 것 같아서 s1 을 작성했다..

'''

import sys
sys.stdin = open('input.txt')


def divide_mat(mat, i):
    """
    특정 열 i를 제거한 행렬 반환

    :param mat: 원본 행렬
    :param i: 제거할 열
    :return: i열을 제거한 행렬
    """
    result = []
    for r in range(len(mat)):
        temp = []
        for c in range(len(mat[0])):
            if c != i:
                temp.append(mat[r][c])
        result.append(temp)
    return result


def find_minsum(mat, N):
    """
    N차 정사각행렬의 최소 합을 찾는 함수

    :param mat: 찾을 행렬
    :param N: 행렬의 차수
    :return: 최소 합
    """
    # N 이 2 이면 한 번만 비교
    if N == 2:
        sum1 = mat[0][0] + mat[1][1]
        sum2 = mat[0][1] + mat[1][0]
        if sum1 > sum2:
            return sum2
        else:
            return sum1

    # N 이 3 이상이면 첫 행과 나머지 행렬 분리하여 비교
    # ex) N=3  | 1 2 3 |       1       2       3
    #          | 4 5 6 | =>  | 5 6 | | 4 6 | | 4 5 |
    #          | 7 8 9 |     | 8 9 | | 7 9 | | 7 8 |
    #
    #     위 3가지에 대해 "첫 행의 항목 + 밑 행렬의 최소합" 의 최소값을 반환
    else:
        # 각 행렬의 항목은 10 이하의 자연수
        min_sum = N * 10
        for i in range(N):
            divided = divide_mat(mat[1:], i)
            temp = mat[0][i] + find_minsum(divided, N-1)
            if temp < min_sum:
                min_sum = temp

        return min_sum


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    result = find_minsum(mat, N)
    print('#{} {}'.format(tc, result))
