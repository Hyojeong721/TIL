import sys
sys.stdin = open('input.txt')

def matrixes(matrix):
    pass




T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    print('#{}'.format(test_case))