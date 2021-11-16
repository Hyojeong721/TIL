import sys
sys.stdin = open('input.txt')

n = int(input())
for i in range(n):
    lst = list(map(int, input()))
    cnt_lst = [0] * 10
    for i in lst:
        cnt_lst[i] += 1


