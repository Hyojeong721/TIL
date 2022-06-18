import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    N, M = list(map(int, input().split()))
    numbers = list(map(int, input().split()))

    segments_sum = []
    for i in range(N-M+1):
        segments_sum.append(sum(numbers[i:i+M]))

    min_value = segments_sum[0]
    max_value= segments_sum[0]
    for number in segments_sum:
        if min_value > number:
            min_value = number
    for number in segments_sum:
        if max_value < number:
            max_value = number
    diff = max_value - min_value

    print('#{0} {1}'.format(t, diff))