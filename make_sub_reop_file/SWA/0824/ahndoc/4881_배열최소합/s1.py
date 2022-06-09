import sys
sys.stdin = open('input.txt')

# 인덱스를 순열로 나열 -> 최소값을 구한다
# def f(i, cursum):
#     global min_v
#
#     if min_v < cursum:
#         return
#
#     if i == N:
#         if min_v > cursum:
#             min_v = cursum
#             return
#     else:
#         for j in range(i, N):
#             P[i], P[j] = P[j], P[i]
#             f(i + 1, cursum + data[i][P[i]])
#             P[i], P[j] = P[j], P[i]
#         return
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     data = [list(map(int, input().split())) for _ in range(N)]
#
#     min_v = 9999999
#     P = list(range(N))
#
#     f(0, 0)
#
#     print('#{} {}'.format(tc, min_v))



def find(i, cursum):
    global ans
    if cursum > ans:
        return

    if i == N:
        # temp = 0
        # for k in range(N):
        #     temp += arr[k][P[k]]
        # if temp < ans:
        #     ans = temp
        if ans > cursum:
            ans = cursum
        return

    else:
        for j in range(i, N):
            # k=0 0,0 1,1 2,2
            # k=1
            # k=2
            P[i], P[j] = P[j], P[i]
            find(i+1, cursum + arr[i][P[i]])
            P[i], P[j] = P[j], P[i]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    P = list(range(N))
    ans = 99999999
    # print(arr)
    find(0, 0)
    print('#{} {}'.format(tc, ans))


