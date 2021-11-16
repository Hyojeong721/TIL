import sys
sys.stdin = open('input.txt')

T = int(input())

def BruteForce(p, t):
    i = 0
    j = 0
    while i < len(p) and j < len(t):
        if p[i] != t[j]:
            j = j - i
            i = -1
        elif p[i] == t[j] and i == len(p)-1:
            return 1
        i += 1
        j += 1
    return 0

for tc in range(1, T + 1):
    str1 = input()
    str2 = input()

    print('#{} {}'.format(tc, BruteForce(str1, str2)))

