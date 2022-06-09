numbers = list(map(int, input().split()))

for num in numbers:
    arr = []
    # 소수 구하기
    sqrt = int(num**(1/2))
    for i in range(1, sqrt+1):
        if num % i == 0:
            arr.append(i)
            if num / i != i:
                arr.append(int(num/i))
        if len(arr) >= 3:
            break

    if len(arr) == 2:
        print("prime number")
    elif len(arr) >= 3:
        print("composite number")
    else:
        print("number one")


