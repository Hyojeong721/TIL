import sys
sys.stdin = open('input.txt')

def tree(n):
    if n <= N:
        tree(n*2)
        tree_list.append(char[n])
        tree(2*n + 1)
    return tree_list

T=10

for tc in range(1,T+1):
    # 정점의 총수 N
    N = int(input())
    char = [0]
    tree_list = []
    # 순서대로 글자 리스트 만들기
    for n in range(N):
        arr = list(input().split())
        char.append(arr[1])

    result = "".join(tree(1))

    print("#{} {}".format(tc, result))