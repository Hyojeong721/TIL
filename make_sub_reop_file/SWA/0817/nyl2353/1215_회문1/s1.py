import sys
sys.stdin = open('input.txt')


def is_palindrome(word):
    """
    문자열 word 가 회문인지 검사하는 함수
    return: 1 또는 0

    """
    if word == word[::-1]:
        return 1
    else:
        return 0


def get_transposed(mat):
    """
    문자열 리스트 mat 의 행과 열을 교환하는 함수
    return: (행렬전치된 새로운 리스트)

    """
    mat_transposed = []
    for r in range(len(mat)):
        word = ''
        for c in range(len(mat)):
            word += mat[c][r]
        mat_transposed.append(word)
    return mat_transposed


def get_num_palindrome(mat, M):
    """
    문자열 리스트로 된 mat 에서 M 길이의 회문을 찾는 함수
    return: (회문의 개수)

    """
    mat_transposed = get_transposed(mat)
    cnt = 0
    for r in range(8):
        for c in range(8 - M + 1):
            sliced_r = mat[r][c : c + M]
            sliced_c = mat_transposed[r][c : c + M]
            cnt += is_palindrome(sliced_r)
            cnt += is_palindrome(sliced_c)
    return cnt


for tc in range(1, 11):
    M = int(input())
    mat = [input() for _ in range(8)]
    result = get_num_palindrome(mat, M)
    print('#{0} {1}'.format(tc, result))