import sys
sys.stdin = open("input.txt")

def half(N, arr):
    for i in range(N):
        while len(arr) < 2:
                if j in range(i, (i + N) // 2 + 1):
                    return rsp(arr)

                elif j in range((i + N)//2+1, j+1):
                    return rsp(arr)

# 나누는 함수
def rsp(arr):
    for i in range(2):
# 2명일 때
        if arr[i] == 1 and arr[i + 1] == 2:
            return (i + 1, 2)
        elif arr[i] == 1 and arr[i + 1] == 3:
            return (i, 1)
        elif arr[i] == 1 and arr[i + 1] == 1:
            return (i, 1)
        elif arr[i] == 2 and arr[i + 1] == 1:
            return (i, 2)
        elif arr[i] == 2 and arr[i + 1] == 2:
            return (i, 2)
        elif arr[i] == 2 and arr[i + 1] == 3:
            return (i + 1, 3)
        elif arr[i] == 3 and arr[i + 1] == 1:
            return (i + 1, 1)
        elif arr[i] == 3 and arr[i + 1] == 2:
            return (i, 3)
        elif arr[i] == 3 and arr[i + 1] == 3:
            return (i, 3)

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    for idx, stud_num in enumerate(arr):
        print(idx, stud_num)

    print(half(N, arr))







