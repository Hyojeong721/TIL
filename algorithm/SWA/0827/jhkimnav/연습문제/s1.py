'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''


# 출력 : 1 2 4 3 5 6

def pre_order(n):
    if n:  # 유효한 정점이면
        print(n)
        pre_order(left[n])
        pre_order(right[n])


V = int(input())
edge = list(map(int, input().split()))
E = V - 1
left = [0] * (V + 1)
right = [0] * (V + 1)

for i in range(E):
    p, c = edge[i * 2], edge[i * 2 + 1]

    # 왼쪽 자식이 아직 없는 경우, 왼쪽 자식으로 저장
    if left[p] == 0:
        left[p] = c
    # right 자식이 있는 경우, 오른쪽 자식으로 저장
    else:
        right[p] = c

# print(left)
# print(right)

pre_order(1)
