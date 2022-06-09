import sys
sys.stdin = open('input.txt')

def binary(a, b):
    num_2 = []
    while b > 0:
        num_2.append(b % 2)
        b //= 2

    return list(reversed(num_2))



T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())


    l = len(binary(N, M))
    status = 1

    if l < N:
        status = 0
    else:
        for i in range(l-N, l):
            if binary(N, M)[i]:
                status = status and 1
            else:
                status = 0

    if status:
        result = 'ON'
    else:
        result = 'OFF'

    print('#{} {}'.format(test_case, result))