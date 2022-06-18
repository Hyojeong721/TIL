import sys
sys.stdin = open('input.txt')

def move(idx, e, c):
    if idx == station[0]:
        return
    else:
        # 배터리 교체하지 않고 내려보내기
        move(idx+1, e-1, c)
        # 배터리를 교체하고 내려보내기
        move(idx+1, station[idx]-1, c+1)


def find(now, cnt):
    global ans
    if ans < cnt:
        return

    battery = station[now]

    if now >= N:
        if ans > cnt:
            ans = cnt
        return

    for i in range(battery, -1, -1):
        if i == 0:
            return
        find(now + i, cnt + 1)

T = int(input())
for tc in range(1, T+1):
    station = list(map(int, input().split())) + [0] * 10
    N = station[0]
    # station = [0] + arr[1:] + [0] * N
    ans = 9999999
    # print(N, station)

    # battery = station[1]
    find(1, -1)
    print('#{} {}'.format(tc, ans))

