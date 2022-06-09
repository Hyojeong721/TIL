# 4836 색칠하기
# 칠이 끝난 후 색이 겹쳐 보라색이 된 칸 수를 구하라

import sys
sys.stdin = open("input.txt")
# 테스트 케이스 개수를 받아온다.
T = int(input())

for tc in range(1, T+1):
    N = int(input())

    # 1: 빨강 2: 파랑 3:보라 0: 빈공간 (흰색)
    table = [[0]*10 for _ in range(10)]
    cnt = 0

    for n in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        # 위에서 아래로
        for i in range(r1, r2+1):
            # 왼쪽에서 오른쪽으로
            for j in range(c1, c2+1):
                table[i][j] += color
                if table[i][j] ==3:
                    cnt += 1
    print('#{} {}'.format(tc, cnt))