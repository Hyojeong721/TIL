n = int(input())

for z in range(n):
    num = int(input())
    cnt = 1
    # 본인이 소수인 경우
    sqrt = int(num **(1/2))
    arr=[]
    for i in range(1, sqrt + 1):
        if num % i == 0:
            arr.append(i)
            if num / i != i:
                arr.append(int(num / i))

    if len(arr) == 2:
        print(num)

    # 본인이 소수가 아닌 경우
    else:
        while 1:
            res = []
            num_sub = num - cnt
            num_sum = num + cnt
            num_list = [num_sub, num_sum]
            sqrt_sub = int(num_sub ** (1 / 2))
            sqrt_sum = int(num_sum ** (1 / 2))
            sqrt_list = [sqrt_sub, sqrt_sum]

            for k in range(2):
                arr = []
                sqrt = sqrt_list[k]
                for i in range(1, sqrt + 1):
                    if num_list[k] % i == 0:
                        arr.append(i)
                        if num_list[k] / i != i:
                            arr.append(int(num_list[k] / i))

                if len(arr) == 2:
                    res.append(num_list[k])
            if res:
                print(*res)
                break

            cnt += 1