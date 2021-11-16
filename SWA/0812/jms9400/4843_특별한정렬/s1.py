import sys
sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    n = int(input())
    numbers = list(map(int, input().split()))


    for i in range(n):

        idx = i
        # max min 의 인덱스만 알면됨

        if i % 2:
            for j in range(i+1, n):
                if numbers[j] < numbers[idx]:
                    idx = j
        else:
            for k in range(i+1, n):
                if numbers[k] > numbers[idx]:
                    idx = k

        numbers[i], numbers[idx] = numbers[idx], numbers[i]

    numbers = ' '.join(map(str, numbers[0:10]))
    print("#{} {}".format(tc, numbers))
