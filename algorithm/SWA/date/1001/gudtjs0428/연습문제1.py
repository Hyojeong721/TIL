# 선택 정렬 함수(SelectionSort)를 재귀적 알고리즘으로 작성해 보시오.
# 6기_A반_Python 응용_완전검색 & 그리디 P14

def selection_sort(l, i=0):
    n = len(l)
    if i == n - 1:
        return l
    min_i = i
    for j in range(i+1, n):
        if l[j] < l[min_i]:
            l[j], l[min_i] = l[min_i], l[j]
    i += 1
    l = selection_sort(l, i)
    return l

print(selection_sort([3,2,1]))