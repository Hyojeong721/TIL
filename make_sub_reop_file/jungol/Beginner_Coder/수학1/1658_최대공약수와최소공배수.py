n, m = map(int, input().split())

# 최대 공약수와 최소 공배수를 출력
def gcd_get(n, m):
    if n < m:
        big = m
    else:
        big = n

    gcd = 0
    for i in range(1, big+1):
        if n % i == 0  and m % i == 0:
            gcd = i
    return gcd

gcd = gcd_get(n, m)
lcm = n * m //gcd
print(gcd)
print(lcm)