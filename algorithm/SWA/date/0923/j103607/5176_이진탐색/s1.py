import sys
sys.stdin = open('input.txt')


def maketree(num):
    global value

    if num <= N:
        maketree(num*2)
        tree[num] = value
        value += 1
        maketree(num*2+1)
    return tree


T = int(input())
for tc in range(1, T+1):
    N = int(input())   # 1~N까지의 숫자를 저장 (=노드 개수)

    # 트리 만들기
    tree = [0 for _ in range(N+1)]
    value = 1
    maketree(1)

    print('#{} {} {}'.format(tc, tree[1], tree[N//2]))