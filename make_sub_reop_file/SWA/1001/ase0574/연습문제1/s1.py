def selection(arr):
    if arr !=[]:
        min_num = min(arr)
        arr.removie(min_num)
        return [min_num] + selection(arr)
    else:
        return []
