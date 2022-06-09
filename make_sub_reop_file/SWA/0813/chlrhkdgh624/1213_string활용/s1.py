import sys
sys.stdin = open('input.txt')

T = 10

for _ in range(T):
    tc = int(input())
    pattern = input()
    text = input()

    i = 0  # text idx
    j = 0  # pattern idx
    cnt = 0

    while i < len(text) and j < len(pattern):
        if text[i] != pattern[j]:
            i = i - j
            j = -1

        i += 1
        j += 1

        if j == len(pattern):
            cnt += 1
            i -= 1
            j = 0

    print(f'#{tc} {cnt}')