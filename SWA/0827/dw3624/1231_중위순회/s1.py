import sys
sys.stdin = open('input.txt')

T = 10
N = int(input())
words = [0] * (N + 1)
left = [0] * (N + 1)
right = [0] * (N + 1)
for n in range(N):
    tmp = list(input().split())
    idx = int(tmp.pop(0))
    words[idx] = tmp.pop(0)
    if tmp:
        left[idx] = int(tmp.pop(0))
    if tmp:
        right[idx] = int(tmp.pop(0))

print(words)
print(left)
print(right)

def tree(n):
    if n:
        print(n, end = ' ')

        tree(n//2)
        tree(n//2+1)

