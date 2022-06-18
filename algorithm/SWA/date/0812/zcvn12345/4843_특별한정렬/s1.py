def selectionSort(a):
    for i in range(0, N, 2):

        max_idx = i
        for j in range(i, N):
            if a[max_idx] < a[j]:
                max_idx = j
        a[i], a[max_idx] = a[max_idx], a[i]

        min_idx = (i+1)
        for j in range(i+1, N):
            if a[min_idx] > a[j]:
                min_idx = j
        a[i+1], a[min_idx] = a[min_idx], a[i+1]


import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    ai = list(map(int, input().split()))
    selectionSort(ai)
    print('#{}'.format(test_case), end=' ')
    for i in range(10):
        print(ai[i], end=' ')
    print()
