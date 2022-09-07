N = 30
def A(n, cnt):
    cnt = 0
    if (n==1) or (n==2):
        return (1, 1)
    else:
        return (A(n-1, cnt)[0] + A(n-2, cnt)[0], cnt+1)

def B(n):

    arr = [0 for _ in range(n)]
    arr[0], arr[1] = 1, 1
    cnt = 0

    for i in range(2, n):
        arr[i] = arr[i-1] + arr[i-2]
        cnt += 1

    return cnt


code_a, code_b = A(N, 1)[0], B(N)
print(code_a, code_b)