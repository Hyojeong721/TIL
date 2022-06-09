# 부분집합  합 문제 구현하기
# 10개의 정수 집합에 대한 모든 부분 집합 중 원소의 합이 0이 되는 집합 출력

def fun_and_sum0(n):
    for i in range(0, (1<<n)):
        temp = 0
        arr_sub = []
        for j in range(0, n):
            if i & (1<<j):
                arr_sub.append(arr[j])
                temp += arr[j]
        if temp == 0:
            print(arr_sub)
    return

arr = [-1, 3,-9, 6, 7, -6, 1, 5, 4, -2]
n = len(arr)

fun_and_sum0(n)