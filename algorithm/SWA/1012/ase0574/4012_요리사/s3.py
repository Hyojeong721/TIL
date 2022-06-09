# pass!

import sys
sys.stdin = open('input.txt')

def food (first , second):
    global min_sub
    a = 0
    b = 0
    # 재료 갯수만큼 반복 더함
    for i in range(len(first)):
        # Sij + Sji 부분
        a += (arr[first[i][0]][first[i][1]] + arr[first[i][1]][first[i][0]])
        b += (arr[second[i][0]][second[i][1]] + arr[second[i][1]][second[i][0]])

    if min_sub > abs(a-b):
        min_sub = abs(a-b)

# 조합1 = 총 재료를 반으로 나누는 조합
def com(n, r, s, k):

    if k == r:
        comb_list.append(comb[:])
        return

    else:
        for i in range(s, n-r+k+1):
            comb[k] = i
            com(n, r, i+1, k+1)

# 조합2 = 한사람의 재료를 2개씩 조합 ex)[0,1,2] -> [[0,1],[0,2],[1,2]]
def comb2(arr):
    result = []
    for i in range(len(arr)):
        for j in arr[i + 1:]:
            result.append((arr[i], j))
    return result

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    comb = [0] * (N//2)
    min_sub = 999999
    comb_list=[]

    com(N, N//2, 0, 0)

    first = comb_list[:len(comb_list)//2]
    second = comb_list[:len(comb_list)//2-1:-1]


    for i in range(len(first)):
        food(comb2(first[i]), comb2(second[i]))

    print("#{} {}".format(tc, min_sub))

