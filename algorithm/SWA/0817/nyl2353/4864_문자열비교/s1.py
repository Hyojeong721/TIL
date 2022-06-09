import sys
sys.stdin = open('input.txt')

def brute_force(pattern, text):
    """
    고지식한 패턴 검색 알고리즘을 이용해 문자열 검사.
    text 에 pattern 문자열이 있으면 True, 없으면 False 를 반환하는 함수.

    """
    M = len(pattern)
    N = len(text)

    for t in range(N - M + 1):
        for p in range(M):
            if text[t] == pattern[p]:
                t += 1
            elif text[t] != pattern[p]:
                break
            if p == M - 1:
                return 1

    return 0

T = int(input())
for tc in range(1, T + 1):
    pattern = input()
    text = input()
    result = brute_force(pattern, text)
    print('#{0} {1}'.format(tc, result))