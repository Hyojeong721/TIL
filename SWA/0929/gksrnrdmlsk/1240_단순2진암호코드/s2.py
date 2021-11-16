import sys
sys.stdin = open('input.txt')

T = int(input())
code = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9
}

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    word = ''
    for _ in range(N):
        word += input()
    for i in range(M * N - 1, -1, -1):
        if word[i] == '1':
            word = word[i-55:i+1]
            break

    result = 0
    answer = 0
    for j in range(8):
        value = code[word[7 * j: 7 * (j + 1)]]

        if j % 2 == 0:
            answer += value
            result += 3 * value
        else:
            answer += value
            result += value

    if result % 10:
        print('#{} {}'.format(tc, 0))
    else:
        print('#{} {}'.format(tc, answer))