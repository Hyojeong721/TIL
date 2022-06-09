while 1:
    user = list(input().split())
    a = int(user[0])
    if a == 0:
        break
    s = user[1]
    b = int(user[2])
    # 1단계 : 10진법으로 바꾸기
    s = int(s, base=a)
    # 2단계 : b진법으로 바꾸기
    arr = []
    jin = [chr(i) for i in range(65, 91)]

    while s >= b:
        remainder = s % b
        if remainder >= 10:
            arr.append(jin[remainder-10])
        else:
            arr.append(remainder)
        s = s // b

    if s > 9:
        arr.append(jin[s - 10])
    else:
        arr.append(s)

    arr.reverse()
    for i in arr:
        print(i, end='')
    print()


