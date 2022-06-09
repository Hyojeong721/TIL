import sys
sys.stdin = open("sample_input.txt")


def my_check(node):
    global cnt

    child_node_l = node * 2
    child_node_r = node * 2 + 1

    if node <= N:
        if child_node_l <= N:
            my_check(child_node_l)

        node_list[node] = cnt
        cnt += 1

        if child_node_r <= N:
            my_check(child_node_r)

T = int(input())
for tc in range(T):
    N = int(input())

    node_list = [0] * (N+1)
    cnt = 1
    my_check(1)
    print('#{} {} {}'.format(tc+1, node_list[1], node_list[N//2]))