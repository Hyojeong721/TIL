import sys
sys.stdin = open('input.txt')

T = int(input())

for T in range(1, T+1):
    # M 리프 노드의 개수, L : 출력할 번호
    N, M, L = list(map(int, input().split()))
    # 짝수일때, 마지막노드 + 1 범위까지 검사하기 위해
    tree = [0] * (N+2)
    # 입력에서 주어진 리프노드의 인덱스와 값을 이용해서
    # tree 배열에 저장
    for _ in range(M):
        idx, value = list(map(int, input().split()))
        tree[idx] = value

    # 총 노드의 수가 짝수일 경우와 홀수일경우 나누어 생각
    # 짝수일 경우 마지막 노드와 해당 노드의 오른쪽 노드를 더해서
    # 부모노드(i를 2로 나눈 정수값)에 저장
    # 홀수일 경우 마지막 노드와 해당 노드의 왼쪽 노드를 더해서
    # 부모노드에 저장
    # 그리고 문제에서 요구하는 L 노드의 값을 출력
    if N % 2 == 0:
        for i in range(N, 1, -2):
            tree[i//2] = tree[i] + tree[i+1]
    else:
        for j in range(N, 2, -2):
            tree[j//2] = tree[j] + tree[j-1]

    print('#{} {}'.format(T, tree[L]))
