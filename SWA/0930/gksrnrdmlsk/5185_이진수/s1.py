import sys
sys.stdin = open('input.txt')
AtoF = {
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15
}

T = int(input())
for tc in range(1, T + 1):
    N, number = input().split()
    N = int(N)
    answer = ''
    for value in number:
        try:
            result = AtoF[value]
        except:
            result = int(value)

        answer += '0' * (4 - len(bin(result)[2:])) + bin(result)[2:]

    print('#{} {}'.format(tc, answer))
