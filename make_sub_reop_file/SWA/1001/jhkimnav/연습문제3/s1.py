'''
모든 부분 집합 중 원소의 합이 0이 되는 부분 집합을 모두 출력하시오.
'''
arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
n = len(arr)
cnt = 0

for i in range(1 << n):
    par_arr = []
    for j in range(n):
        if i & (1 << j):
            par_arr.append(arr[j])
    if sum(par_arr) == 0:
        print(par_arr)
