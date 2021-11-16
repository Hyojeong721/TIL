import sys
sys.stdin = open('input.txt')

T = int(input())

for i in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))
    max_number = numbers[0]
    min_number = numbers[0]

    for number in numbers:
        if max_number < number:
            max_number = number

        if min_number > number:
            min_number = number

    result = max_number - min_number
    print('#{} {}'.format(i+1, result))

