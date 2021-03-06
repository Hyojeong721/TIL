'''
정점의 갯수와 간선 정보
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13

6
1 2 1 3 2 4 3 5 3 6
'''
def pre_order(n):
    if n:           # 유효한 정점이면
        print(n)
        pre_order(left[n])    # n의 왼쪽 자식으로 이동
        pre_order(right[n])

V = int(input())
edge = list(map(int, input().split()))
E = V - 1           # V개의 정점이 있는 트리의 간선 수
left = [0]*(V+1)     # 부모를 인덱스로 자식번호 저장
right = [0]*(V+1)
for i in range(E):
    p, c = edge[i*2], edge[i*2+1]
    if left[p] == 0:    # p의 왼쪽 자식이 없으면
        left[p] = c
    else:               # 왼쪽 자식이 있으면 오른쪽 자식으로 저장
        right[p] = c

pre_order(1)