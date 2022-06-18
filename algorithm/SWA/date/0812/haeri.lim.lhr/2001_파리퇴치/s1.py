import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    total = 0
    arr=[]
    delta =[
        [0, -1],
        [0, 1],
        [-1, 0],
        [1, 0]
    ]

    for i in range(N):
        temp = list(map(int, input().split()))
        arr.append(temp)

    for i in range(N):
        for j in range(N):
            for d in delta:
                if 0 <= i+d[0] < N and 0 <= j+d[1] < N:
                    total += abs(arr[i][j] - arr[i+d[0]][j+d[1]])

    print(total)