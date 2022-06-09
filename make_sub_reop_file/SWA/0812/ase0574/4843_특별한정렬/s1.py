import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    new_list = []

    if N % 2:
        K = N//2+1
    else:
        K = N//2

    for k in range(K):
        max_number = arr[0]
        min_number = arr[0]
        if len(arr) >= 2:
            for i in range(len(arr)):
                if max_number < arr[i]:
                    max_number = arr[i]
                elif min_number >= arr[i]:
                    min_number = arr[i]
            new_list.append(max_number)
            new_list.append(min_number)
            arr.remove(max_number)
            arr.remove(min_number)
        else:
            new_list.append(arr[len(arr)-1])

    result = new_list[0:10]

    print('#{}'.format(tc), *result)
