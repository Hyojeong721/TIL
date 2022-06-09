import sys
sys.stdin = open('input.txt')

def absoulte(arr):
    return up(arr) + down(arr) + left(arr) + right(arr)

def up(arr):
    try:
        if i-1 >= 0:
            return abs(arr[i][j] - arr[i - 1][j])
        else:
            return 0
    except:
        return 0

def down(arr):
    try:
        return abs(arr[i][j] - arr[i + 1][j])
    except:
        return 0

def left(arr):
    try:
        if j-1 >= 0:
            return abs(arr[i][j] - arr[i][j - 1])
        else:
            return 0
    except:
        return 0

def right(arr):
    try:
        return abs(arr[i][j] - arr[i][j + 1])
    except:
        return 0


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    total = 0

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            total += absoulte(arr)

    print('#{0} {1}'.format(test_case, total))
