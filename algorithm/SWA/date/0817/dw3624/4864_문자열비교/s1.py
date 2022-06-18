import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    char = input()
    text = input()
    n = len(char)
    result = 0

    for i in range(n, len(text) + 1):
        if char == text[i-n:i]:
            result = 1
            break
    print('#{} {}'.format(t, result))