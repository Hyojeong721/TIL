import sys
sys.stdin = open("input.txt")

for tc in range(1,int(input())+1):
    N = int(input())
    load=[]
    for _ in range(N):
        load.append(int(input()))

    print(load)