import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    str_datas = [input() for _ in range(N)]

    # 가로
    for i in range(N - M + 1):
        for data in str_datas:
            if data[i:i+M] == data[i:i+M][::-1]:
                print('#{} {}'.format(tc, data[i:i+M]))
                break
    # 세로
    for j in range(N):
        temp = ''
        for data in str_datas:
            temp += data[j]
        for i in range(N - M + 1):
            if temp[i:i+M] == temp[i:i+M][::-1]:
                print('#{} {}'.format(tc, temp[i:i+M]))