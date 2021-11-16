import sys
sys.stdin = open('input.txt')

T = int(input())
def make(num):
    heap.append(num)
    index = len(heap)-1

    while index>1 and heap[index] < heap[index//2]:
        heap[index], heap[index//2] = heap[index//2], heap[index]
        index //= 2

def sum_heap(N):
    ans = 0
    index = N//2

    while index:
        ans += heap[index]
        index //= 2
    return ans

for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    heap = [0]

    for num in arr:
        make(num)

    print("#{} {}".format(tc, sum_heap(N)))



