import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N, M = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    for i in range(M):
        x = arr.pop(0)
        arr.append(x)

    print('#{} {}'.format(test_case, arr[0]))