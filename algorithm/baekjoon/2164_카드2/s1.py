import sys
from collections import deque

N = int(sys.stdin.readline())
arr = deque()

for i in range(1, N+1):
    arr.append(i)
# print(arr)
k = 1
while len(arr) != 1:
    if 0 == k%2:
        temp = arr.popleft()
        arr.append(temp)
    else:
        arr.popleft()
    k += 1

print(arr[0])