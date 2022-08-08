import sys
sys.stdin = open('input.txt')

N = int(input())
arr = list(map(int, input()))
res = 0

for n in range(N):
    res += arr[n]


print(res)