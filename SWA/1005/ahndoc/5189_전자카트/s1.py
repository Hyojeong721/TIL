import sys
sys.stdin = open('input.txt')

def find(curpos, cursum):
    global ans

    if ans < cursum:
        return

    if 0 not in visited:
        cursum += arr[curpos][0]
        if ans > cursum:
            ans = cursum
        return

    else:
        for j in range(N):
            if not visited[j]:
                visited[j] = 1
                find(j, cursum + arr[curpos][j])
                visited[j] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    visited[0] = 1
    ans = N * 100
    find(0, 0)
    print('#{} {}'.format(tc, ans))




# def find(s, cursum, visited):
#     global ans
#     if ans < cursum:
#         return
#
#     if len(visited) == N:
#         cursum += arr[s][0]
#         if ans > cursum:
#             ans = cursum
#
#     else:
#         for i in range(N):
#             if i != s and i not in visited:
#                 find(i, cursum + arr[s][i], visited + [i])
#
#
#     # global ans, sum_v
#     # if cursum > ans:
#     #     return
#     #
#     # visited[curpos] = 1
#     # if 0 not in visited:
#     #     cursum += arr[curpos][0]
#     #     if cursum < ans:
#     #         ans = cursum
#     #     return
#     # else:
#     #     for i in range(N):
#     #         if i != curpos and i not in visited:
#     #             find(i, cursum + arr[curpos][i])
#     #     visited[curpos][i] = 0
#
#
#
#     # global ans, sum_v
#     # if ans < sum_v:
#     #     # return
#     #
#     #     visited[i] = 1
#     #
#     #     if 0 not in visited: # 방문을 다 했다면
#     #         sum_v += arr[i][0]
#     #         if sum_v < ans:
#     #             ans = sum_v
#     #         sum_v -= arr[i][0]
#     #         return
#     #     else:      # 미방문이 있다면,
#     #         for j in range(N):
#     #             if not visited[j]:
#     #                 sum_v += arr[i][j]
#     #                 find(j)
#     #                 sum_v -= arr[i][j]
#     #         visited[i] = 0
#
#
#     # if i == N:
#     #     # print(Q)
#     #     print(P)
#     #     print(P[::-1])
#     #     return
#     # else:
#     #     for j in range(i, N):
#     #         P[i], P[j] = P[j], P[i]
#     #         # Q[i], Q[j] = Q[j], Q[i]
#     #         if P[0] == 0:
#     #             find(i+1, cursum)
#     #             P[i], P[j] = P[j], P[i]
#     #             # Q[i], Q[j] = Q[j], Q[i]
#
#
# # [0, 1, 2]
# # [0, 2, 1]
# # [0, 1, 2, 3]
# # [0, 1, 3, 2]
# # [0, 2, 1, 3]
# # [0, 2, 3, 1]
# # [0, 3, 2, 1]
# # [0, 3, 1, 2]
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     ans = 9999999999
#     cursum = 0
#     P = list(range(N))
#     Q = list(range(N))
#     C = [0] * N
#
#     # visited = [0] * N
#     visited = [0]
#     print(arr)
#     # print(P)
#     find(0, 0, visited)
#     print(ans)
#     # for i in range(N):
#     #     for j in range(i+1, N):
#
#     # N = 3일 때, 인덱스 1~2 : 0 1 2 0 / 0 2 1 0
#     # [0][1] [1][2] [2][0] / [0][2] [2][1] [1][0]
#     # N = 4일 때, 인덱스 1~3 : 0 1 2 3 0 / 0 1 3 2 0 / 0 2 1 3 0 / 0 2 3 1 0 / 0 3 1 2 0 / 0 3 2 1 0
#     # [0][1] [1][2] [2][3] [3][0] / [0][1] [1][3] [3][2] [2][0] / [0][2] [2][1] [1][3] [3][0]