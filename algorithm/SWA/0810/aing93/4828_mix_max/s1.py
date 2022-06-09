import sys
sys.stdin = open('input.txt')

# T = int(input())
#
# for i in range(1, T+1):
#     N, numbers = int(input()), list(map(int, input().split()))
#     min = numbers[0]
#     max = numbers[0]
#     for number in numbers:
#         if min > number:
#             min = number
#
#     for number in numbers:
#         if max < number:
#             max = number
#
#     diff = max - min
#     print('#{0} {1}'.format(i, diff))
# Min Max
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    max = numbers[0]
    min = numbers[0]
    for i in numbers:
        if i > max:
            max = i
    for j in numbers:
        if j < min:
            min = j
    diff = max - min

    print('#{} {}'.format(tc, diff))

