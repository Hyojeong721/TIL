import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, K = list(map(int, input().split()))
    lst = [([0] + list(map(int, input().split())) + [0]) for i in range(N)]
    lst.insert(0, [0] * (N + 2))
    lst.append([0] * (N + 2))
    cnt = 0

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if lst[i][j] == 1:
                try:
                    if sum(lst[i][j:j + K]) == K and lst[i][j + K] == 0 and lst[i][j-1] == 0:
                        cnt += 1
                except:
                    pass


                try:
                    temp = 0
                    for number in range(i, i + K):
                        temp += lst[number][j]
                    if temp == K and lst[i + K][j] == 0 and lst[i-1][j] == 0:
                        cnt += 1
                except:
                    pass

    print('#{} {}'.format(tc, cnt))


