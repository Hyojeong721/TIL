import sys
sys.stdin = open('input.txt')

T = int(input())

def bfs(x):
    global N, cnt
    cnt += 1

    # N이 10보다 작으면 앞에 0을 붙여서 두자리수 만들고
    if x < 10:
        x = '0' + str(x)
    else:
        x = str(x)

    # 각 자리의 숫자를 더한다
    sum_num = str(int(x[0]) + int(x[1]))

    # 주어진 수의 오른쪽 자리 수와
    # 합의 가장 오른쪽 자리수를 이어 붙이면 새로운 수
    new = x[1] + sum_num[-1]

    if int(new) == N:
        return
    else:
        bfs(int(new))
    return

for tc in range(T):
    # 0 <= N <= 99
    N = int(input())
    cnt = 0

    bfs(N)

    print(cnt)
