import sys
sys.stdin = open('input.txt')
T = int(input())

def paste_sol(N):
    for tc in range(1, T+1):
        if N == 10:
            return 1

        elif N == 20:
            return 2

        else:
            return 
