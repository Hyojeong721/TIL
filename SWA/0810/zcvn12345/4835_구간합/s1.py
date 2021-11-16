import sys
sys.stdin = open('input.txt')

T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    sums = []
    for j in range(N-M+1):
        temp = 0
        for number in range(M):
            temp += numbers[j+number]
        sums.append(temp)
    max_value = sums[0]
    min_value = sums[0]
    for index in range(len(sums)):
        if max_value < sums[index]:
            max_value = sums[index]
        if min_value > sums[index]:
            min_value = sums[index]
    result = max_value - min_value
    print('#{0} {1}'.format(i + 1, result))


