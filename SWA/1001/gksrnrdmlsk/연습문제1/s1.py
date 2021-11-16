
def rec_sort(lst):
    if len(lst) == 1:
        return lst
    else:
        idx = 0
        minimum = lst[idx]
        for i in range(len(lst)):
            if lst[i] < minimum:
                minimum = lst[i]
                idx = i
        lst.pop(idx)
        return [minimum] + rec_sort(lst)

print(rec_sort([10, 7, 4, 6, 3, 2, 5, 7, 1, 3, 6]))
print(sorted([10, 7, 4, 6, 3, 2, 5, 7, 1, 3, 6]))