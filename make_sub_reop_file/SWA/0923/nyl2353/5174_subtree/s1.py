import sys
sys.stdin = open('input.txt')


def find_child(p):
    """
    p를 부모로 가진 자식 노드 c가 있으면 num_child 를 1 증가시키고,
    c를 부모로 갖는 자식 노드를 찾아 나가는 함수

    parent 배열
    c | 0 1 2 3 4 5 6
    p | 0 2 0 5 6 2 1
    """
    global num_child

    for c in range(1, E + 2):
        # c: 자식, p: 부모
        if parent[c] == p:
            num_child += 1
            find_child(c)


T = int(input())
for tc in range(1, T + 1):
    E, N = map(int, input().split())
    lst = list(map(int, input().split()))

    # 부모를 저장 ex) [0 2 0 5 6 2 1]
    parent = [0] * (E + 2)
    for i in range(E):
        up = lst[2 * i]
        down = lst[2 * i + 1]
        parent[down] = up

    num_child = 1
    start = N
    find_child(start)

    print('#{} {}'.format(tc, num_child))
