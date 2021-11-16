import sys
sys.stdin = open("input.txt")


def is_palindrome(word):
    """주어진 문자열이 회문인지 검사한다.

    Returns:
        문자열이 회문이면 True, 아니면 False
    """
    for i in range(len(word) // 2):
        if word[i] != word[-(i + 1)]:
            return False
    return True


def get_palindrome(words, N, pld_length):
    """단어 리스트 words의 가로/세로에 존재하는 회문을 구한다.

    Args:
        N: 단어의 개수, 단어 하나의 길이 (int)
        pld_length: 찾아야 하는 회문의 길이 (int)
    Returns:
        words 내에 존재하는 회문 (str)
    """

    # 1. 가로 회문 탐색
    for r in range(N):
        for c in range(N - pld_length + 1):
            current = words[r][c:c + pld_length]
            if is_palindrome(current):
                return current

    # 2. 세로 회문 탐색
    for c in range(N):
        for r in range(N - pld_length + 1):
            current = ''
            for i in range(r, r + pld_length):
                current += words[i][c]

            if is_palindrome(current):
                return current


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    words = []

    for _ in range(N):
        words.append(input())

    pld = get_palindrome(words, N, M)

    print("#{} {}".format(tc, pld))
