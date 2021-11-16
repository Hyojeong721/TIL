import sys
sys.stdin = open("input.txt")


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    numbers = [int(x) for x in input().split()]

    print("#{} {}".format(tc, numbers[M % N]))
