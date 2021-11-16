import sys
sys.stdin = open('input.txt', 'r')


def calc(arr, i):
    total = 1
    for x in range(i):
        total *= ability[x][arr[x]]/100
    return total * 100


def efficiency(arr, i):
    global maximum
    if calc(arr, i) < maximum:
        return
    if i == N:
        if calc(arr, i) > maximum:
            maximum = calc(arr, i)
            return
    else:
        for j in range(N):
            if allocated[j]:
                arr[i] = j
                allocated[j] = 0
                efficiency(arr, i+1)
                arr[i] = -1
                allocated[j] = 1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ability = [list(map(int, input().split())) for _ in range(N)]
    allocated = [1]*N  # 해당 일이 이미 할당되었는지 체크
    role = [-1]*N
    maximum = 0
    efficiency(role, 0)
    print(tc, maximum)

