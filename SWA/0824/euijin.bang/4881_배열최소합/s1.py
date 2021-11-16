import sys
sys.stdin = open("input.txt")

import itertools

# pool = ['A', 'B', 'C']
# print(list(map(''.join, itertools.permutations(pool)))) # 3개의 원소로 수열 만들기
# print(list(map(''.join, itertools.permutations(pool, 2)))) # 2개의 원소로 수열 만들기

def permute(arr):
    result = [arr[:]]
    c = [0] * len(arr)
    i = 0
    while i < len(arr):
        if c[i] < i:
            if i % 2 == 0:
                arr[0], arr[i] = arr[i], arr[0]
            else:
                arr[c[i]], arr[i] = arr[i], arr[c[i]]
            result.append(arr[:])
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1
    return result

T = int(input())

for tc in range(1, T+1):

    N = int(input())

    arr = [list(map(int, input().split())) for _ in range (N)]

    max_total = 0
    result = []
    for i in range(N):
        for j in range(len(arr)):
            print(permute(arr[j]))
