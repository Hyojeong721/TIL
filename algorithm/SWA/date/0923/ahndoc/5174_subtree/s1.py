import sys
sys.stdin = open('input.txt')

# def preorder(T):
#     global cnt
#     if T == 0:
#         return
#     cnt += 1
#     preorder(left[T])
#     preorder(right[T])
#
#
# for tc in range(1, int(input()) + 1):
#     E, N = map(int, input().split())
#     arr = list(map(int, input().split()))
#     # 구현1
#     left = [0] * (E + 2)  # 첫번째 자식
#     right = [0] * (E + 2)  # 두번째 자식
#     # 구현2
#     for i in range(0, len(arr), 2):
#         p, c = arr[i], arr[i + 1]  # 부모 - 자식
#         if left[p]:  # 0이 아니고 첫번째에 값이 있으면
#             right[p] = c  # 두번째에 보관
#         else:  # 0이면
#             left[p] = c  # 첫번째에 보관
#     # print(left, right)
#     cnt = 0
#     preorder(N)
#     print('#{} {}'.format(tc, cnt))

def preorder(n):
    global cnt
    if n:
        cnt += 1
        preorder(left[n])
        preorder(right[n])

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    edge = list(map(int, input().split()))
    # E: 간선의 개수
    left = [0] * (E+2)
    right = [0] * (E+2)
    for i in range(E):
        p, c = edge[i*2], edge[i*2+1]
        if left[p]:
            right[p] = c
        else:
            left[p] = c
    # print(left, right)
    cnt = 0
    preorder(N)

    print('#{} {}'.format(tc, cnt))