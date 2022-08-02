import sys
sys.stdin = open("input.txt")
from itertools import combinations

N, M = map(int, input().split())
arr = {}
for _ in range(N):
    guitar, music = input().split()
    arr[guitar] = music

guitars = list(arr.keys())

res = -1
cnt = 0

def check(join):
    temp = [False] * M
    for j in join:
        able = arr[j]
        for k in range(M):
            if able[k] == 'Y':
                temp[k] = True
    return temp.count(True)


for i in range(1, N+1):
    jo = list(combinations(guitars, i))
    for j in jo:
        temp_cnt = check(j)
        if cnt < temp_cnt:
            cnt = temp_cnt
            res = len(j)

print(res)