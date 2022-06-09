import sys
sys.stdin = open('input.txt')


def inorder(num):

    global result
    if num <= N:
        inorder(num*2)
        result += temp[num]
        inorder(num*2+1)


T = 10
for tc in range(1, T+1):

    N = int(input())   # 노드 총 개수

    temp = [0]*(N+1)
    for i in range(N):
        info = list(input().split())   # 노드 번호, 해당 알파벳. (왼쪽 노드 번호), (오른쪽 노드 번호)
        temp[int(info[0])] = info[1]

    result = ''
    inorder(1)
    print('#{} {}'.format(tc, result))
