import sys
sys.stdin = open('input.txt')

T = 10

for test_case in range(1,T+1):
    N = int(input())
    arr = []
    result = []
    l_diagonal = r_diagonal = 0

    for i in range(100):
        temp = list(map(int, input().split()))
        arr.append(temp)

    for i in range(len(arr)):
        r_sum = 0
        for j in range(len(arr[i])):
            r_sum += arr[i][j]
        result.append(r_sum)

        l_diagonal += arr[i][i]
        r_diagonal += arr[i][len(arr) - 1 - i]
    result.append(l_diagonal)
    result.append(r_diagonal)

    for j in range(len(arr[i])):
        c_sum = 0
        for i in range(len(arr)):
            c_sum += arr[i][j]
        result.append(c_sum)

    print('#%d %d' %(test_case, max(result)))