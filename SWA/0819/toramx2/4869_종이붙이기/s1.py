import sys
sys.stdin = open('input.txt')

def attach(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        return attach(n-1) + 2 * attach(n-2)

T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    result = attach(N // 10)
    print('#{0} {1}'.format(test_case, result))

