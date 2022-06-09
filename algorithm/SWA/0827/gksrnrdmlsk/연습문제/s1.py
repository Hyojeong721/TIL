import sys
sys.stdin = open('input.txt')

def preorder(n):
    print(n)
    if left[n]:
        preorder(left[n])
    if right[n]:
        preorder(right[n])

def inorder(n):
    if left[n]:
        inorder(left[n])
    print(n)
    if right[n]:
        inorder(right[n])

def postorder(n):
    if left[n]:
        postorder(left[n])
    if right[n]:
        postorder(right[n])
    print(n)


V = int(input())
lst = list(map(int, input().split()))
E = V - 1
left = [0] * (V + 1)
right = [0] * (V + 1)
for i in range(E):
    if not left[lst[2 * i]]:
        left[lst[2 * i]] = lst[2 * i + 1]
    else:
        right[lst[2 * i]] = lst[2 * i + 1]

inorder(1)
postorder(1)