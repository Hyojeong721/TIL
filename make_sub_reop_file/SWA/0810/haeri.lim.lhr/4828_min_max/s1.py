import sys
sys.stdin = open('input.txt')

T = int(input())

for i in range(T):
    N = int(input())
    temp = list(map(int, input().split()))

    min = temp[0]
    max = temp[0]

    for j in range(N):
        if temp[j] >= max:
            max = temp[j]
        elif temp[j] <= min:
            min = temp[j]

    print('#%d %d'%(i+1,max-min))
