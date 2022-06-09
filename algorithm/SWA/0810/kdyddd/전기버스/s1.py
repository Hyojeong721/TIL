import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):

    answer = 0
    value = list(map(int, input().split()))
    K = value[0]
    N = value[1]
    M = value[2]
    battery = list(map(int, input().split()))

    position = 0
    i = 0
    cnt = 0
    while position + K < N:
        while i < len(battery) and battery[i] <= position + K:
            i += 1

        cnt += 1

        if i >= len(battery):
            break

        if battery[i] - battery[i-1] > K:
            cnt = 0
            break

        position = battery[i-1]

    answer = cnt
    print(f'#{test_case} {answer}')