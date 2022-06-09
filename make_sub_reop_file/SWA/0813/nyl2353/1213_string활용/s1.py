import sys
sys.stdin = open('input.txt')

def brute_force(pattern, text):
    """
    text를 처음부터 끝까지 차례대로 순회하면서 pattern 과 일치하는 문자들의 갯수를 세는 함수
    text: 한 문장
    pattern: 검색할 문자열

    """
    M = len(pattern)
    N = len(text)

    cnt = 0
    for t in range(N - M + 1):
        for p in range(M):
            if text[t] == pattern[p]:
                t += 1
            elif text[t] != pattern[p]:
                break
            if p == M - 1:
                cnt += 1
    return cnt

for _ in range(10):
    tc = int(input())
    pattern = input()
    text = input()
    result = brute_force(pattern, text)
    print('#{0} {1}'.format(tc, result))
