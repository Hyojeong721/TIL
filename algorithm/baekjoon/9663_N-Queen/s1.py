# N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.
# N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.
# 퀸은 직선과 대각선으로 움직일 수 있다.

N = 8
arr = [0] * N

ans = 0

def check(x):
    global N, arr
    for k in range(x):
        if arr[x] == arr[k] or abs(arr[x] - arr[k])== x-k:
            return False
    return True

def queen(x):
    global N, arr, ans

    if x == N:
        ans += 1
        return ans

    else:
        for i in range(N):
            arr[x] = i
            if check(x):
                queen(x+1)

queen(0)
print(ans)