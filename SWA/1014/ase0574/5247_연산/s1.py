# N->M을 만들때 사용할 수 있는 연산이 +1, -1, *2, -10 네 가지
# 최소 몇번의 연산을 거쳐야하는지

# 제한시간 초과
import sys
sys.stdin = open('input.txt')


def bfs(n):
    global ans, M

    q.append(n)
    while q:
        qt=[]
        temp = q.pop(0)

        for t in range(len(temp)):
            for i in range(len(temp[t])):

                if 0 < temp[t][i] < 1000000:
                    if temp[t][i] == M:
                        return

                    else:
                        if temp[t][i] not in visited:
                            visited.append(temp[t][i])
                            qt.append([temp[t][i]+1, temp[t][i]-1, temp[t][i]*2, temp[t][i]-10])
        q.append(qt)
        ans+=1

T = int(input())

for tc in range(1, T+1):
    N, M = input().split()
    N = int(N)
    M = int(M)
    ans = 0
    q = []
    visited = []

    bfs([[N]])

    print("#{} {}".format(tc, ans))