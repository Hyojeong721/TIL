import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    # 10 X 10 리스트 생성
    arr = [[0] * 10 for _ in range(10)]
    for _ in range(N):
        x1, y1, x2, y2, color = map(int, input().split())

        # 사각형들이 차지한 좌표를 1로 더해주기
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                arr[i][j] += color

    # 겹친 사각형 넓이 계산
    count = 0
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 3:
                count += 1
    print('#{} {}'.format(test_case, count))