import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    n = int(input())
    building = list(map(int, input().split()))
    second_num = 0
    result = 0

    for i in range(0, n-4):

        temp = max(building[i:i+5])

        if temp == building[i+2]:
            for j in range(5):
                if j == 2:
                    pass
                elif building[i+j] >= second_num:
                    second_num = building[i+j]
            result += temp - second_num
        second_num = 0

    print('#{} {}'.format(tc, result))
