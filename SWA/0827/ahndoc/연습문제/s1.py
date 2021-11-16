import sys
sys.stdin = open('input.txt')

# 전위 순회
def pre_order(n):
    if n:
        print(n)
        pre_order(left[n])
        pre_order(right[n])
# 중위 순회
def in_order(n):
    if n:
        in_order(left[n])
        print(n)
        in_order(right[n])
# 후위 순회
def post_order(n):
    if n:
        post_order(left[n])
        post_order(right[n])
        print(n)


V = int(input())
edge = list(map(int, input().split()))
E = V - 1
left = [0] * (V+1)
right = [0] * (V+1)
par = [0] * (V+1) # 자식을 인덱스로 부모번호 저장


# 부모가 없으면 root
root = 1
while par[root]: # root로 추정한 정점이 부모가 있으면
    root += 1
print(root)

for i in range(E):
    p, c = edge[i*2], edge[i*2+1]
    if left[p] == 0:
        left[p] = c
    else:
        right[p] = c
    par[c] = p      # (1) 조상을 찾는데 사용
                    # (2) root 찾기 (포화이진트리의 정점 규칙을 사용하지 않는 이진트리를 다룰 때 사용)

# 조상 찾기
c = 6
while par[c]:
    print(par[c])
    c = par[c]

# pre_order(3)
# 서브트리의 정점의 개수
# 서브트리의 자손의 수 (루트를 제외하고 카운트)