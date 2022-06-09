import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    numbers = list(map(int, input().split()))

    for i in range(1, 1 << len(numbers)):
        total = 0
        for j in range(len(numbers)):
            if i & (1 << j):
                total += numbers[j]

        if total == 0:
            result = 1
            break
        else:
            result = 0

    print('#{0} {1}'.format(test_case, result))