import sys
sys.stdin = open('input.txt')


def in_order(n):  # 중위 순회
    if n <= N:
        in_order(n * 2)  # 왼쪽 자식
        print(tree[n], end='')  # 루트
        in_order(n * 2 + 1)  # 오른쪽 자식


for tc in range(1, 11):
    N = int(input())  # 총 정점의 수
    tree = [[0] for _ in range(N + 1)]
    for i in range(N):
        info = input().split()  # 정점 정보 입력
        tree[int(info[0])] = info[1]  # 인덱스 = 노드 번호, 값 = 노드 값
    print('#{}'.format(tc), end=' ')
    in_order(1)
    print()



