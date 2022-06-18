import sys
sys.stdin = open('input.txt')

T = 1

for test_case in range(1,T+1):
    N = int(input())
    arr =[]

    for i in range(100):
        temp = list(map(int, input().split()))
        arr.append(temp)
    for c in range(len(arr)):
        i = 0
        j = c
        l_condition = j != 0 and arr[i][j - 1] == 1
        r_condition = j != len(arr)-1 and arr[i][j + 1] == 1

        while arr[i][j] == 1 and j < len(arr[0])-1 and i < len(arr)-1:

            if l_condition or r_condition:
                while l_condition:
                    j -= 1
                    if j != 0 and arr[i][j + -1] == 0:
                        i += 1
                        break

                while r_condition:
                    j += 1
                    if j != len(arr)-1 and arr[i][j + 1] == 0:
                        i += 1
                        break

            else:
                i += 1

            if arr[i][j] == 2:
                print('#%d %d' % (test_case, c))
                break

