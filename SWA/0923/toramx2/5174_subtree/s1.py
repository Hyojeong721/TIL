import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    E, N = list(map(int, input().split()))
    node_pair = list(map(int, input().split()))
    sub = [N]       # 서브 트리의 노드를 담을 list
    queue = [N]     # 부모 노드를 임시 저장할 list

    while queue:
        curr = queue.pop()
        for i in range(0, 2*E, 2):              # 부모 노드만 검색하면서
            if node_pair[i] == curr:            # 부모 노드의 자식이 있다면
                sub.append(node_pair[i+1])      # 자식 노드를 sub에 저장
                queue.append(node_pair[i+1])    # 자식 노드를 queue에 저장해 자손 노드 확인

    print('#{} {}'.format(test_case, len(sub)))