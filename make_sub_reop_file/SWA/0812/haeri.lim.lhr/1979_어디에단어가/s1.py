import sys
sys.stdin = open('input.txt')

T = 10

for test_case in range(1,T+1):
    N = int(input())
    delta =[
        [0, -1],
        [0, 1],
        [-1, 0],
        [1, 0]
    ]
    arr =[]

    for i in range(100):
        temp = list(map(int, input().split()))
        arr.append(temp)

    for c in range(len(arr)):
        i = 0
        j = c
        while i < len(arr[0])-1 and j < len(arr)-1:
            if arr[i+delta[2][0]][j+delta[2][1]] == 1:
                i += delta[2][0]
                j += delta[2][1]
            elif arr[i + delta[3][0]][j + delta[3][1]] == 1:
                i += delta[3][0]
                j += delta[3][1]
            else:
                i += delta[1][0]
                j += delta[1][1]

            if arr[i][j] == 2:
                print('#%d %d' %(test_case, c))
                break

