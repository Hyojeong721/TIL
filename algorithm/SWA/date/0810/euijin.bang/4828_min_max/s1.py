import sys
sys.stdin = open('input.txt')

T = int(input())

# N = number of positive numbers
# max_num : the largest number
# min_num : the smallest number

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    # temporary max and min number
    max_num = numbers[0]
    min_num = numbers[0]

    # finding max and min number with for statement
    for i in range(N):
        if max_num < numbers[i]:
            max_num = numbers[i]

        if min_num > numbers[i]:
            min_num = numbers[i]

    ans = max_num - min_num

    print("#{} {}".format(tc, ans))