import sys
sys.stdin = open('input.txt')

T = int(input())


def BruteForce(pattern, text):
    M = len(pattern)
    N = len(text)
    i = 0
    j = 0
    cnt = 0

    while i < M and j < N:
        if text[j] != pattern[i]:
            j = j - i
            i = -1
        i += 1
        j += 1

        if i == M:
            cnt += 1
            i = 0
            j -= 1

    if cnt > 0:
        return 1
    else:
        return 0


for tc in range(1, T + 1):
    str1 = input()
    str2 = input()
    result = BruteForce(str1, str2)
    print(f'#{tc} {result}')


