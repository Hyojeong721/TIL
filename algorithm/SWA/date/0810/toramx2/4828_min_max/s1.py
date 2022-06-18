import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):
    N, numbers = int(input()), list(map(int, input().split()))
    min_value = numbers[0]
    max_value = numbers[0]

    for number in numbers:
        if min_value > number:
            min_value = number

    for number in numbers:
        if max_value < number:
            max_value = number

    diff = max_value - min_value

    print('#{0} {1}'.format(test_case, diff))