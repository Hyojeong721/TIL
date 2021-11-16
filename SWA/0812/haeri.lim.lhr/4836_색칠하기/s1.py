import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    arr = []
    for i in range(N):
        temp = list(map(int, input().split()))
        arr.append(temp)
