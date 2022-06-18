import sys
sys.stdin = open("input.txt")


def get_max_length(words):
    """
    문자열 배열을 인자로 받아, 가장 긴 문자열의 길이를 구한다.

    Args:
        words: 문자열 배열
    Returns:
        max_length: 가장 긴 문자열의 길이
    """
    max_length = 0

    for word in words:
        if len(word) > max_length:
            max_length = len(word)

    return max_length


def traverse_vertically(words):
    """
    문자열 배열을 인자로 받아, 세로로 순회한다.
    ex. words = ['abc', '12', 'DEF']인 경우,
        a => 1 => D => b => 2 => E => c => F의 순서로 순회한다.

    Args:
        words: 문자열 배열
               (단, 문자열의 길이는 서로 다를 수 있다.)
    Returns:
        total: 문자열 배열 전체를 세로로 순회한 문자열 (위 예시의 경우, 'a1Db2EcF')
    """
    total = ""
    max_length = get_max_length(words)

    for c in range(max_length):
        for word in words:
            # 해당 문자열의 마지막 인덱스가 c 이상이라면
            if len(word) > c:
                total += word[c]

    return total


T = int(input())

for tc in range(1, T + 1):
    words = []
    for _ in range(5):
        words.append(input())

    result = traverse_vertically(words)
    print("#{} {}".format(tc, result))
