import sys
from itertools import permutations
sys.stdin = open('input.txt')
def cal(n1, n2, ex_idx, oper):
    idx = ex_idx - 1
    if oper[idx] == '+':
        return n1 + n2
    elif oper[idx] == '-':
        return n1 - n2
    elif oper[idx] == '*':
        return n1 * n2
    else:
        if n1 < 0 :
            temp = abs(n1) // n2
            return -temp
        else:
            return n1 // n2

N = int(input())
numbers = list(map(int, input().split()))
oper_cnt = list(map(int, input().split()))
oper_temp = []
for o in range(4):
    if o == 0:
        oper_temp = oper_temp + ['+'] * oper_cnt[o]
    elif o == 1:
        oper_temp = oper_temp + ['-']*oper_cnt[o]
    elif o==2:
        oper_temp = oper_temp + ['*'] * oper_cnt[o]
    else:
        oper_temp = oper_temp + ['/'] * oper_cnt[o]

opers = set(list(permutations(oper_temp, N-1)))

max_res = -1e9
min_res = 1e9
for oper in opers:
    temp = numbers[0]
    for i in range(1, N):
        temp = cal(temp, numbers[i], i, oper)
    max_res = max(temp, max_res)
    min_res = min(temp, min_res)

print(max_res)
print(min_res)