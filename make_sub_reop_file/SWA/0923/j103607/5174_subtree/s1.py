import sys
sys.stdin = open('input.txt')



def countnode(num):

    global count
    for i in range(2):
        if table[i][num]:
            count += 1
            next_num = table[i][num]
            countnode(next_num)
    return count


T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())   # E: 간선 개수 N: 루트 노드 번호
    tree = list(map(int, input().split()))

    # 표 만들기
    table = [[0]*(E+2) for _ in range(2)]

    for i in range(E):
        p = tree[i*2]
        c = tree[i*2+1]

        if table[0][p] == 0:
            table[0][p] = c
        else:
            table[1][p] = c

    count = 1
    countnode(N)

    print('#{} {}'.format(tc, count))