import sys
sys.stdin = open('input.txt')
T = 10

for tc in range(1, T + 1):
    length = int(input())
    lst = [list(input()) for i in range(8)]
    result = 0
    for r in range(8): # 행별로 탐색합니다.
        for c in range(8 - length + 1):
            if lst[r][c:c + length] == lst[r][c:c + length][::-1]:
                result += 1

    for c in range(8): # 열별로 탐색합니다.
        for r in range(8 - length + 1):
            if [lst[r + i][c] for i in range(length)] == [lst[r + i][c] for i in range(length)][::-1]:
                result += 1

    print('#{} {}'.format(tc, result))