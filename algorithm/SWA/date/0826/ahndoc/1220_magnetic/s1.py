import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 1은 아래로, 2는 위로 향함
    cnt = 0
    for j in range(N):
        temp = ''              # 세로줄 모든 자성체 ('1', '2')를 temp에 합산
        for i in range(N):
            if arr[i][j] == 1:
                temp += '1'
            if arr[i][j] == 2:
                temp += '2'
        cnt += temp.count('12')   # 교착개수('1', '2' 순서로 붙어있는 부분)를 카운트

    print('#{} {}'.format(tc, cnt))