import sys
sys.stdin = open('input.txt')

T = 10

for test_case in range(1, T + 1):
    num = int(input())
    building = list(map(int, input().split()))
    answer = 0
    for i in range(2, num -2):
        max_height = 0
        for j in range(1, 3):
            if building[i-j] > max_height:
                max_height = building[i-j]

            if building[i+j] > max_height:
                max_height = building[i+j]

        if building[i] > max_height:
            answer += building[i] - max_height

    print(f'#{test_case} {answer}')