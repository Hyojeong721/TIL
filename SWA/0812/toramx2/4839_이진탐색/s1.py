import sys
sys.stdin = open('input.txt')

def binarysearch_count(book, key):
    left = 0
    right = len(book) - 1
    count = 0

    while left <= right:
        count += 1
        center = int((left + right) / 2)
        if book[center] == key:
            break
        elif book[center] > key:
            right = center
        else:
            left = center

    return count

T = int(input())

for test_case in range(1, T+1):
    P, Pa, Pb = list(map(int, input().split()))
    book = list(range(1, P+1))

    if binarysearch_count(book, Pa) < binarysearch_count(book, Pb):
        result = 'A'
    elif binarysearch_count(book, Pa) > binarysearch_count(book, Pb):
        result = 'B'
    else:
        result = 0

    print('#{0} {1}'.format(test_case, result))