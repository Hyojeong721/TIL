import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N 세로 M 가로
    arr = [list(input()) for _ in range(N)]
    temp = []
    answer = []

    for i in range(N):
        for j in range(M):
            if arr[i][j] == '1':
                if arr[i][j+54] == '1':
                    temp = arr[i][j-1:j+55]
                    break
                elif arr[i][j+53] == '1':
                    temp = arr[i][j-2:j+54]
                    break
                elif arr[i][j+52] == '1':
                    temp = arr[i][j-3:j+53]
                    break
        if len(temp) != 0:
            break

    password = {
        '0001101': 0,
        '0011001': 1,
        '0010011': 2,
        '0111101': 3,
        '0100011': 4,
        '0110001': 5,
        '0101111': 6,
        '0111011': 7,
        '0110111': 8,
        '0001011': 9,
    }
    for k in range(0, 56, 7):
        temp2 = ''.join(temp[k:k+7])
        answer.append(password[temp2])

    total = 0
    for a in range(len(answer)):
        if a % 2 == 0:
            total += answer[a] * 3
        else:
            total += answer[a]
    if total % 10 == 0:
        print('#{} {}'.format(tc, sum(answer)))
    else:
        print('#{} {}'.format(tc, 0))