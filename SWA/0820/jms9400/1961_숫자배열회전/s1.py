import sys
sys.stdin = open('input.txt')

T = int(input())


def spin_arr(arr1, arr2):
    for i in range(N):
        temp = ''
        for j in range(N-1, -1, -1):
            temp += arr1[j][i]
        arr2.append(temp)
    return arr2


for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]

    arr_90 = []
    arr_180 = []
    arr_270 = []

    spin_arr(arr, arr_90)
    spin_arr(arr_90, arr_180)
    spin_arr(arr_180, arr_270)

    print('#{}'.format(tc))
    for n in range(N):
        print(arr_90[n], arr_180[n], arr_270[n])
