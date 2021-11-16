import sys
sys.stdin = open('input.txt')

def mid_left_right(n, info):
    global string
    if info[n*2]:
        n *= 2
        mid_left_right(n, info)
    if info[n*2+1]:




T = int(input())
for text_case in range(1, T + 1):
    N = int(input())
    info = [[] for _ in range(N + 1)]
    for i in range(1, N + 1):
        info[i] = input().split()
    string = ''