import sys
sys.stdin = open("test.txt")

t = int(input())
for tc in range(1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    print(arr)