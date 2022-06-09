import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    answer = 0
    N = int(input())

    # 색이 칠해질 10 * 10 격자 생성
    arr = [[0] * 10 for i in range(10)]

    for n in range(N):
        y1, x1, y2, x2, color = list(map(int, input().split()))
        for i in range(y1, y2+1):
            for j in range(x1, x2+1):

                # 어떤 색이 칠해져 있고, 그 색이 현재 칠할 색과 다르다면 겹침
                if arr[i][j] != 0 and arr[i][j] != color:
                    answer += 1

                # 겹친 부분이 없다면, 해당 색을 표시!
                else:
                    arr[i][j] = color

    print('#{} {}'.format(test_case, answer))