import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    words = [input() for _ in range(5)]
    result = ''

    for c in range(15):
        for r in range(5):
            if len(words[r]) > c:
                result += words[r][c]

    print('#{0} {1}'.format(tc, result))
