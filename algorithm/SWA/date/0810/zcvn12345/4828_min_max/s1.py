import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    max_value = numbers[0]
    min_value = numbers[0]
    for j in range(1, N):
        if max_value < numbers[j]:
            max_value = numbers[j]
        if min_value > numbers[j]:
            min_value = numbers[j]
    result = max_value - min_value
    print('#{0} {1}'.format(test_case, result))


