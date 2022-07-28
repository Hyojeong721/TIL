import sys
sys.stdin = open('input.txt')


N = int(input())
arr = list(map(int, input().split()))
arr.sort()
M = int(input())
numbers = list(map(int, input().split()))

def binary(s, e, num):
    if s > e:
        return 0

    mid = (s + e) // 2
    if arr[mid] == num:
        return 1
    elif num < arr[mid]:
            return binary(s, mid-1, num)
    else:
            return binary(mid+1, e, num)

for num in numbers:
    print(binary(0, N-1, num))

