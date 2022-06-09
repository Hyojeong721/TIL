import sys
sys.stdin = open('input.txt')

T = int(input())

def selectionSort(a):
    result = []
    for i in range(0, len((a))-1):
        min = i
        for j in range(i+1, len(a)):
            if a[min] > a[j]:
                min = j
        a[i], a[min] = a[min], a[i]

    for i in range(5):
        result.append(a[len(a)-1-i])
        result.append(a[i])

    result = ' '.join(map(str, result))
    return result



for tc in range(1, T+1):
    numbers_len = int(input())
    numbers = list(map(int, input().split()))

    print('#{0} {1}'.format(tc, selectionSort(numbers)))
