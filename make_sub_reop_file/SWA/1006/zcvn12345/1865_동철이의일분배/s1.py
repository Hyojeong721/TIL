import sys
sys.stdin = open('input.txt')

T = int(input())




for tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    q = []
    for i in range(0, N):
        q.append([0, (i,), (mat[0][i])])
    while q:
        if q[0][0] == N-1:
            break
        a = q.pop(0)
        for i in range(N):
            if i not in a[1]:
                b = a[:]
                b[0] += 1
                b[1] += (i,)
                b[2] *= (mat[a[0]][i])
                q.append(b)
    prob_lst = []
    for j in q:
        prob_lst.append(j[2])
    print(q)
    print(max(prob_lst))