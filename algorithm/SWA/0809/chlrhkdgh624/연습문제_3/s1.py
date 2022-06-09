import sys

sys.stdin = open('input.txt')

N = int(input())
print('Test case:', N)

for i in range(N):
    j = int(input())
    boxes = list(map(int, input().split()))
    for k in
