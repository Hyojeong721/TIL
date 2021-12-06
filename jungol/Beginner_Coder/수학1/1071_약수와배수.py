# 정수의 개수 n (1<=n<=40) ->numbers의 갯수
n = int(input())
# n개의 정수
numbers = list(map(int, input().split()))
# 약수와 배수를 구할 정수m (1<=m<=100)
m = int(input())
aliquot = 0
multiple = 0

for i in numbers:
    if bool((m / i) - (m // i) == 0):
        aliquot += i
    if bool((i / m) - (i // m) == 0):
        multiple += i

print(aliquot)
print(multiple)
