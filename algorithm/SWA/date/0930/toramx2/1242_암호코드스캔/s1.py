import sys
sys.stdin = open('input.txt')

PATTERN= {
    '0': '0001101',
    '1': '0011001',
    '2': '0010011',
    '3': '0111101',
    '4': '0100011',
    '5': '0110001',
    '6': '0101111',
    '7': '0111011',
    '8': '0110111',
    '9': '0001011',
}

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    code = ''
    for _ in range(N):
        code += input()

    print(code)