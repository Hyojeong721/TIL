def pre_order(n):
    if n:       # 유효한 정점이면
        print(n)
        pre_order(left[n])      # n의 왼쪽자식으로 이동
        pre_order(right[n])

def in_order(n):
    if n:
        in_order(left[n])
        print(n)
        in_order(right[n])

def post_order(n):
    if n:
        post_order(left[n])
        post_order(right[n])
        print(n)

V = int(input())
edge = list(map(int, input().split()))
E = V - 1
left = [0]*(V+1)             # 부모를 인덱스로 자식번호 저장
right = [0]*(V+1)
par = [0]*(V+1)             # 자식을 인덱스로 부모를 저장


for i in range(E):
    p, c = edge[i*2], edge[i*2+1]
    if left[p] == 0:        # p의 왼쪽자식이 없으면
        left[p] = c
    else:                   # 왼쪽자식이 있으면 오른쪽자식으로 저장
        right[p] = c
    par[c] = p              # 조상 찾기

pre_order(1)