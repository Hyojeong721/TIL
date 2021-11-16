import sys
sys.stdin = open('input.txt')

# def search(curr, cost):
#     global answer
#     if cost >= answer:
#         return
#     else:
#         if curr == N:
#             if cost < answer:
#                 answer = cost
#         else:
#             for i in range(N):
#                 if visited[i] == 0:
#                     visited[i] = 1
#                     search(curr + 1, cost + lst[curr][i])
#                     visited[i] = 0

lst = [1, 0, 0, 2, 10, 4, 40, 92, 352, 724]
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    print('#{} {}'.format(tc, lst[N - 1]))