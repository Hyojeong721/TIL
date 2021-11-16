import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    text = [input() for _ in range(5)]
    long = 0

    for phrase in text:
        if len(phrase) > long:
            long = len(phrase)

    for i in range(5):
        if len(text[i]) < long:
            text[i] += '*' * (long-len(text[i]))

    result = ''
    for col in range(long):
        for row in range(5):
            result += text[row][col]

    print(f'#{tc} {result.replace("*", "")}')
