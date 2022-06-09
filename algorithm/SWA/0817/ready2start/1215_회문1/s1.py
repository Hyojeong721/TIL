import sys
sys.stdin = open('input.txt')


def is_palindrome(word):
    """주어진 문자열이 회문인지 검사한다.
    Returns:
        주어진 문자열이 회문이면 True, 회문이 아니면 False
    """
    for i in range(len(word) // 2):
        if word[i] != word[-(i + 1)]:
            return False
    return True


def count_palindrome(board, N, M):
    """문자열로 이루어진 배열에서 특정 길이의 가로/세로 회문의 개수를 구한다.
    Args:
        board: 문자열 배열
        N: 문자열 하나의 길이 및 문자열의 개수
        M: 회문의 길이
    Returns:
        count: 문자열 배열 내의 길이 M의 회문의 개수
    """
    count = 0

    # 회문의 길이가 1인 경우, 회문의 개수는 곧 문자의 개수
    if M == 1:
        return N * N

    # 1. 가로 회문 탐색
    for r in range(N):
        for c in range(N - M + 1):
            # current: board[r][c]에서 시작하는 길이 M의 가로 부분 문자열
            current = board[r][c:c + M]

            if is_palindrome(current):
                count += 1

    # 2. 세로 회문 탐색
    for c in range(N):
        for r in range(N - M + 1):
            # current: board[r][c]에서 시작하는 길이 M의 세로 부분 문자열
            current = ''
            for cnt_r in range(r, r + M):
                current += board[cnt_r][c]

            if is_palindrome(current):
                count += 1

    return count


T, N = 10, 8

for tc in range(1, T + 1):
    M = int(input())
    board = []

    for _ in range(N):
        board.append(input())

    count = count_palindrome(board, N, M)
    print("#{} {}".format(tc, count))
