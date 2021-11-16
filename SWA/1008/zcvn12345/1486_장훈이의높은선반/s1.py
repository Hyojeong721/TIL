import sys
sys.stdin = open('input.txt')

T = int(input())

def subset(arr, n):
    global result
    for i in range(1 << n):
        temp = 0
        for j in range(n):
            if i & (1 << j):
                temp += arr[j]
        if temp >= B:
            if temp < result:
                result = temp

for tc in range(1, T+1):
    N, B = map(int, input().split())
    nums = list(map(int, input().split()))
    lst = []
    result = 1000000000000000
    subset(nums, N)
    print(f'#{tc} {result-B}')