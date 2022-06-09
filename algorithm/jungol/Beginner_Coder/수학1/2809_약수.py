n = int(input())
sqrt = int(n**(1/2))
arr= [True]*10000
cnt = 0

for i in range(1, sqrt+1):
    if n % i == 0:
        arr[cnt] = i
        cnt += 1
        if n / i != i:
            arr[cnt] = int(n / i)
            cnt += 1

arr = arr[:cnt]
arr.sort()
print(*arr)