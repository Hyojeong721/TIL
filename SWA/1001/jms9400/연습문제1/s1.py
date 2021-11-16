def SelectionSort(lst):

    n = len(lst)
    if n <= 1:
        return lst

    Mi = 0
    for i in range(n):
        if lst[Mi] > lst[i]:
            Mi = i
    lst[0], lst[Mi] = lst[Mi], lst[0]
    return [lst[0]] + SelectionSort(lst[1:])




a = [5, 3, 2, 1, 5, 7, 6, 8]
print(SelectionSort(a))
print(a)  # 왜 처음 순서바뀐 것만 반영되어 있지..?