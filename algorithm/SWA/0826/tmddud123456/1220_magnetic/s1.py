import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    mat = []
    for _ in range(N):
        temp = list(map(int, input().split()))
        mat.append(temp)
    # n극과 s극이 만나는 횟수
    ns = 0
    for i in range(N):
        for j in range(N):
            # mat가 1인 지점 = n극 = 밑으로 떨어진다
            # = 2를 만나면 ns += 1
            # 1을 만날 경우 => 어짜피 for문을 돌면서 방금 만난 1을 기준으로 다시 서치를 하기 때문에 신경을 안써도 된다
            # 아무것도 안 만날 경우 => 떨어지기 때문에 신경 X
            if mat[i][j] == 1:
                k = 1
                if i == 99:
                    pass
                else:
                    while i+k != 99 and mat[i+k][j] == 0:
                        k += 1
                    if mat[i+k][j] == 2:
                        ns += 1

    print('#{} {}'.format(tc, ns))