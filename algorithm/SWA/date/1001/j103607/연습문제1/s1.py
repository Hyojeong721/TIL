'''
선택 정렬 함수(SelectionSort)를 재귀적 알고리즘으로 작성
아직 덜 했음
'''

# def SelectionSort(k):
#     if k:
#         sm = min(k)
#         k.remove(sm)
#         return [sm] + SelectionSort(k)
#     else:
#         return []
#
#
# nums = [5, 7, 8, 9, 3, 1, 6]
# print(SelectionSort(nums))


def selection_sort(my_list):
    for i in range(1, len(my_list)):
        if my_list[i] < my_list[i-1]:
            my_list[i], my_list[i-1] = my_list[i-1], my_list[i]
    return


some_list = [11, 3, 6, 4, 12, 1, 2]
print(selection_sort(some_list))
