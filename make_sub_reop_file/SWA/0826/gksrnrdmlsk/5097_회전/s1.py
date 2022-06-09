import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    front = 0
    rear = N - 1
    front = (front + M) % N
    rear = (rear + M) % N
    print('#{} {}'.format(tc, lst[front]))