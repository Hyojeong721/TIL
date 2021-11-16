import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):

    n = input()
    numbers = list(map(int, input().split()))

    min_num = numbers[-1]
    max_num = numbers[0]

    for number in numbers:
        if number >= max_num:
            max_num = number

        elif number < min_num:
            min_num = number

    min_max = max_num - min_num

    print('#{} {}'.format(test_case, min_max))