n, k = map(int, input().split())

# N의 약수들 중 K번째로 작은 수를 출력
# N은 1 이상 10,000 이하이다. K는 1 이상 N 이하이다.

arr = []
for i in range(1, n+1):
    if n % i == 0:
        arr.append(i)

if len(arr) >= k:
    print(arr[k-1])
else:
    print(0)