m, n = map(int, input().split())

def prime_list(m, n):
    arr = [i for i in range(m, n+1)]
    for i in range(m, n+1):
        i#의 약수
        sqrt = i*i
        for j in range(sqrt, n+1, i):
            if j in arr:
                arr.remove(j)
                print(j)

    if 1 in arr:
        arr.remove(1)
    return len(arr), arr

print(prime_list(m, n))