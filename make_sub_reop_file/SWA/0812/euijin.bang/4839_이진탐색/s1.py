import sys
sys.stdin = open("input.txt")

T = int(input())

def binarySearchcounter (theValue, target):

    # 인덱스이 0 아닌 페이지 1로 시작함에 주의! 인덱스 접근 아님.
    low = 1
    high = theValue

    count = 0

    while low <= high:
        count += 1
        mid = (high + low) // 2

        if mid == target:
            return count

        elif target < mid:
            high = mid
        else:
            low = mid

for tc in range(1, T + 1):
    pages, keyA, keyB = map(int, input().split())

    A_count = binarySearchcounter(pages, keyA)
    B_count = binarySearchcounter(pages, keyB)

    if A_count == B_count:
        result = 0

    elif A_count > B_count:
        result = "B"
    else:
        result = "A"

    print("#{} {}".format(tc, result))