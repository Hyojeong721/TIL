import sys
sys.stdin = open("sample_input.txt")


def preorder_traverse(n):
    """
    주어진 이진 트리에서 노드 N을 루트로 하는
    서브 트리에 속한 노드의 개수를 알아내는 함수
    """
    global cnt

    if n:
        cnt += 1 # 유효한 정점이면 갯수 하나 증가
        preorder_traverse(left[n]) # n의 왼쪽 자식으로 이동
        preorder_traverse(right[n]) # n의 오른쪽 자식으로 이동

    return cnt

T = int(input())
for tc in range(T):
    E, N = map(int, input().split()) # 간선의 개수 E, 루트노드 N, 정점수 V = E+1
    node_nums = list(map(int,input().split()))
    V = E + 1
    cnt = 0

    # 부모를 인덱스로 자식번호 저장, 정점수+1 개의 배열 생성
    left = [0] * (V+1)
    right = [0] * (V+1)

    for i in range(E):
        p, c = node_nums[i*2], node_nums[i*2+1]

        if left[p] == 0: # p의 왼쪽자식이 없으면 왼쪽 자식으로 저장
            left[p]= c
        else:
            right[p]= c # p의 왼쪽자식이 있으면 오른쪽 자식으로 저장

        result = preorder_traverse(N)
        print('#{} {}'.format(tc+1, result))