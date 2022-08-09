import sys
sys.stdin = open('input.txt')

N = int(input())
arr = [int(input()) for _ in range(N)]

arr.sort()

for n in range(N):
    print(arr[n])