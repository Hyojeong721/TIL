import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, code = input().split()
    result = ''
    for i in range(int(N)):
        num = int(code[i], 16)
        for j in range(3, -1, -1):
            if num & (1 << j):
                result += '1'
            else:
                result += '0'

    print('#{} {}'.format(tc, result))