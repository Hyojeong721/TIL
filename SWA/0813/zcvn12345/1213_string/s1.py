import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    test_case = int(input())
    p = input()
    t = input()
    M = len(p)
    N = len(t)
    i = 0
    j = 0
    result = 0
    while j < M and i < N:
        if t[i] == p[j]:
            i += 1
            j += 1
            if j == M:
                result += 1
                j = 0
        else:
            i = i - j + 1
            j = 0
    print('#{0} {1}'.format(tc, result))

