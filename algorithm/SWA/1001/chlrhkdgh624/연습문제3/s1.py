# 부분집합 합 문제 구현하기: binary counting
sample_set = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
n = len(sample_set)
subsets = []

for i in range(0, (1 << n)): # 1 << n = 2**n : 부분 집합의 개수
    subset = []
    for j in range(0, n):
        if i & (1 << j):
            subset.append(sample_set[j])
    if sum(subset) == 0:
        subsets.append(subset)

print(subsets)


