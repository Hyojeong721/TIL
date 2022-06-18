import sys
sys.stdin = open('input.txt')
def search(arr, num, position):
    global ans
    # num = 찾는 정수
    # position = 왼쪽-1 가운데0 오른쪽-1
    # arr = 찾을 리스트

    start, end = 0, len(arr)-1

    while start <= end:
        mid = (start+end)//2

        if num == arr[mid]:
            ans += 1
            return
        elif num < arr[mid]:
            if position == -1:
                return
            end = mid - 1
            position = -1
        elif num > arr[mid]:
            if position == 1:
                return
            start = mid + 1
            position = 1


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = list(map(int, input().split()))
    ans = 0

    for b in range(M):
        search(A, B[b], 0)


    print("#{} {}".format(tc, ans))