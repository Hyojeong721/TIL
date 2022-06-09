import sys
sys.stdin = open('input.txt')

T = 10

def inorder(key, array):

    if key >= len(array):
        return

    elif array[key] != 0:
        inorder(2*key, array)
        print(array[key], end='')
        inorder(2*key+1, array)


for tc in range(1, T+1):
    N = int(input())

    res = [0] * (N+1)
    for i in range(N):
        data = list(input().split())
        idx = int(data[0])
        char = data[1]
        res[idx] = char

    print(f'#{tc} ', end='')
    inorder(1, res)
    print()
