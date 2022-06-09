# 1953.[모의 SW 역량테스트] 탈주범 검거
# 1952.[모의 SW 역량테스트] 수영장
# 1949.[모의 SW 역량테스트] 등산로 조성

import sys
sys.stdin = open('input.txt')

def inorder(node):
    global answer
    if len(lst[node]) == 3:
        inorder(lst[node][1])
        answer += lst[node][0]
        inorder(lst[node][2])
    elif len(lst[node]) == 2:
        inorder(lst[node][1])
        answer += lst[node][0]

    else:
        answer += lst[node][0]

T = 10
for tc in range(1, T + 1):
    answer = ''
    N = int(input())
    lst = [[] for _ in range(N + 1)]
    for i in range(1, N + 1):
        temp = input().split()
        lst[i].append(temp[1])
        if len(temp) >= 3:
            for j in temp[2:]:
                lst[i].append(int(j))
    inorder(1)
    print('#{} {}'.format(tc, answer))


