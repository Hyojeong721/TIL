import sys
sys.stdin = open('input.txt')
# 3장의 카드가 연속적인 경우 run
# 3장의 카드가 동일한 경우 triplet
# 6장의 카드가 run+triplet 인 경우 baby-gin
T = int(input())

for tc in range(1):
    arr = list(map(int, input()))

    # triplet 검사
    for i in range(len(arr)):
        if

def counting_sort(a,b,k)
# a[] 입력정렬
# b[] 정렬된 배열
# c[] 카운트 배열

    c = [0] * k
    for i in range(0,len(b)):
        c[a[i]] += 1
    for i in range(1, len(c)):
        c[i] += c[i-1]
    for i in range(len(b)-1,-1,-1):
        b[c[a[i]]-1] = a[i]
        c[a[i]] += -1