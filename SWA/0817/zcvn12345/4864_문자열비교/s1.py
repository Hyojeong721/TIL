import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = input()
    M = input()
    if N in M:
        print('#{0} 1'.format(tc))
    else:
        print('#{0} 0'.format(tc))