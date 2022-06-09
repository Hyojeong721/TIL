import sys
sys.stdin = open('input.txt')

T = int(input())
def tree(n):
    global cnt
    if n <=N:
        tree(n*2)
        index[n] = cnt
        cnt += 1
        tree(n*2+1)

for tc in range(1,T+1):
    N = int(input())
    cnt = 1
    index = [0 for _ in range(N+1)]
    tree(1)
    print("#{} {} {}".format(tc,index[1], index[N//2]))
