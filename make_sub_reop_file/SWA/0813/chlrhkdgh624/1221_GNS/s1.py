import sys
sys.stdin = open('GNS_test_input.txt')

T = int(input())

patterns = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for tc in range(1, T+1):
    N = int(input().lstrip(f'#{tc} '))
    text = input()
    cnts = [0] * 10

    for pattern in patterns:
        i = 0
        j = 0
        while i < len(text) and j < len(pattern):
            if text[i] != pattern[j]:
                i = i - j
                j = -1

            i += 1
            j += 1

            if j == len(pattern):
                cnts[patterns.index(pattern)] += 1
                i -= 1
                j = 0

    print(f'#{tc}')
    for idx, count in enumerate(cnts):
        for k in range(count):
            print(patterns[idx], end=' ')








