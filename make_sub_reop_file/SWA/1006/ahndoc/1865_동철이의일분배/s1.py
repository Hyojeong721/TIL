import sys
sys.stdin = open('input.txt')

# def find(k, p):
#     global ans
#     if p <= ans:
#         return
#
#     if k >= N:
#         ans = p
#         return
#
#     else:
#         for i in range(N):
#             if not used[i]:
#                 used[i] = 1
#                 find(k+1, p * arr[k][i])
#                 used[i] = 0
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(lambda x: int(x)/100, input().split())) for _ in range(N)]
#     used = [0] * N
#     ans = 0
#
#     find(0, 100)
#
#     print('#{} {:6f}'.format(tc, ans))

def find(r, percentage):
    global ans

    if ans >= percentage:
        return

    if r == N:
        ans = percentage
        return

    for i in range(N):
        if not used[i]:
            used[i] = 1
            find(r+1, percentage * arr[r][i])
            used[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(lambda x: x/100, map(int, input().split()))) for _ in range(N)]
    used = [0] * N
    ans = 0
    find(0, 100)
    print('#{} {:6f}'.format(tc, ans))






