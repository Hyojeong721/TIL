a = [3, 5, 1, 2, 4]

# def selection_sort(A):
#     n = len(A)
#     for i in range(0, n-1):
#         minI = i
#         for j in range(i+1, n):
#             if A[j] < A[minI]:
#                 minI = j
#         A[minI], A[i] = A[i], A[minI]
#     return A
#
# print(selection_sort([3,2,1]))

def selectionSort(xs):
    if xs != []:
        smallest = min(xs)
        xs.remove(smallest)
        return [smallest] + selectionSort(xs)
    else:
        return []

print(selectionSort(a))