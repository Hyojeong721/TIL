# 0830
import sys
sys.stdin = open('input.txt')
# N개의 영역에 대해 왼쪽 위와 오른쪽 아래 모서리 인덱스, 칠할 색상이 주어질 때,
# 칠이 끝난 후 색이 겹쳐 보라색이 된 칸 수를 구하는 프로그램을 만드시오.
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # 왼상x, 왼상y, 오하x, 오하y, 컬러(1=빨강, 2=파랑)
    arr = [list(map(int,input().split())) for _ in range(N)]
    red_list = []
    blue_list = []
    cnt = 0

    for n in range(N):
        if arr[n][4] == 1:
            red_left_x = arr[n][0]
            red_left_y = arr[n][1]
            red_right_x = arr[n][2]
            red_right_y = arr[n][3]
            # 빨강영역
            for i in range(red_left_x, red_right_x + 1):
                for j in range(red_left_y, red_right_y + 1):
                    red_list.append([i, j])

        else:
            blue_left_x = arr[n][0]
            blue_left_y = arr[n][1]
            blue_right_x = arr[n][2]
            blue_right_y = arr[n][3]
            # 파랑영역
            for m in range(blue_left_x, blue_right_x+1):
                for n in range(blue_left_y, blue_right_y+1):
                    blue_list.append([m, n])

    if len(red_list) < len(blue_list):
        for b in blue_list:
            if b in red_list:
                cnt += 1
    else:
        for r in red_list:
            if r in blue_list:
                cnt += 1
    print("#{} {}".format(tc,cnt))

