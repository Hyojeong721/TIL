import sys
sys.stdin = open("input.txt")


def count_substring(word, substring):
    """문자열 내의 부분 문자열의 개수를 구한다.

    단, 겹쳐져 있는 부분 문자열은 세지 않는다.
    예를 들어, count_substring('ABABABA', 'ABA')의 경우
    'ABABABA' 내에 'ABA'는 3개지만
    겹치지 않는 'ABA'는 2개이므로 2를 반환한다.

    Args:
        word: 부분 문자열을 찾을 문자열
        substring: 부분 문자열
    Returns:
        문자열(word) 내의 겹치지 않는 부분 문자열(substring)의 개수
    """
    idx, count = 0, 0
    N, M = len(word), len(substring)

    while idx < N - M + 1:
        if word[idx:idx + M] == substring:
            count += 1
            # 부분 문자열이 겹치지 않도록 부분 문자열이 끝난 다음 인덱스로 이동
            idx += M
        else:
            idx += 1

    return count


T = int(input())

for tc in range(1, T + 1):
    A, B = input().split()

    # a_in_b_count: A 안에 B가 겹치지 않고 존재하는 개수
    a_in_b_count = count_substring(A, B)
    # typing_count: A를 타이핑하기 위해 눌러야 하는 최소 횟수
    typing_count = len(A) - (a_in_b_count * (len(B) - 1))

    print("#{} {}".format(tc, typing_count))
    