import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    result = list(map(int,input().split()))
    print('#{} {}'.format(test_case, max(result)-min(result)))