import sys
sys.stdin = open('input.txt')

# T = int(input())
# for tc in range(1, T+1):
#     K, N, M = map(int, input().split())
#     M_list = list(map(int, input().split()))
#     station = [0] * (N+1)
#     for m in M_list:
#         station[m] = 1
#     cnt = 0
#     bus = K
#     if bus > N:
#         cnt = 1
#     while bus < N:
#         for i in range(bus, bus-K, -1):
#             if station[i]:
#                 cnt += 1
#                 bus = i
#                 break
#         else:
#             cnt = 0
#             break
#         bus += K
#     print('#{} {}'.format(tc, cnt))

T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    M_list = list(map(int, input().split()))
    cnt = [0] * (N+1)
    for i in M_list:
        cnt[i] = 1
    bus = K
    ans = 0
    while bus < N:
        for i in range(bus, bus-K, -1):
            if cnt[i] == 1:
                ans += 1
                bus = i
                break
        else:
            ans = 0
            break
        bus += K

    print('#{} {}'.format(tc, ans))




