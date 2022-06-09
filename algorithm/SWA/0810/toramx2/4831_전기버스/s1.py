import sys
sys.stdin = open('input.txt')

T = int(input())

for i in range(1, T+1):
    K, N, M = list(map(int, input().split()))
    charge = list(map(int, input().split()))
    current = 0
    count = 0

    while current <= N:
        tmp = current

        for step in range(K, 0, -1):

