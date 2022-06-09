import sys
sys.stdin = open('input.txt')

n = int(input())
res = [11]*n
members = list(map(int, input().split()))

for i in range(n):
    cnt = 0
    for k in range(n):
        if res[k]==11 and cnt == members[i]:
            res[k] = i+1
            break
        if res[k] > i+1:
            cnt += 1

print(*res)