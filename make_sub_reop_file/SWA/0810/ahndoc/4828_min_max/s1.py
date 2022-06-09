import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    max_value = numbers[0]
    min_value = numbers[0]

    for number in numbers[1:]:
        if number > max_value:
            max_value = number

    for number in numbers[1:]:
        if number < min_value:
            min_value = number

    result = max_value - min_value

    print('#{} {}'.format(test_case, result))

