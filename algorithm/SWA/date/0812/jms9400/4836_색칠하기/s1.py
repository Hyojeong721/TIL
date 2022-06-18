import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    red = []
    blue = []
    result = 0

    # red와 blue 각각 나눠주기
    for i in range(len(arr)):
        if arr[i][-1] == 1:
            red.append(arr[i][0:4])
        else:
            blue.append(arr[i][0:4])

    # red와 blue 개수만큼 반복
    for n in range(len(red)):
        for m in range(len(blue)):
            # 겹치는 부분의 가로 세로 길이 측정
            w_box = 0
            h_box = 0
            for i in range(red[n][0], red[n][2]+1):
                if i in range(blue[m][0], blue[m][2]+1):
                    w_box += 1
            for j in range(red[n][1], red[n][3] + 1):
                if j in range(blue[m][1], blue[m][3] + 1):
                    h_box += 1
            result += w_box * h_box

    print('#{} {}'.format(tc, result))

    # table 에 각각의 숫자를 색칠하고 그 숫자가 겹치는 부분을 추출하는 방법도 있음! (아래 코드 참고하기)
    # table = [[0]*10 for _ in range(10)]
    # cnt = 0
    #
    # for n in range(N):
    #     r1, c1, r2, c2, color = map(int, input().split())
    #     # 위에서 아래로
    #     for i in range(r1, r2+1):
    #         # 왼쪽에서 오른쪽으로
    #         for j in range(c1, c2+1):
    #             table[i][j] += color
    #             if table[i][j] ==3:
    #                 cnt += 1
    # print('#{} {}'.format(tc, cnt))