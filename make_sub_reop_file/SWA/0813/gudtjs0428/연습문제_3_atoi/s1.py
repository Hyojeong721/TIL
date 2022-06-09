def atoi(string):
    num = 0
    for i in range(1, len(string) + 1):
        num += (ord(string[-i]) - 48) * 10 ** (i - 1)
    return num

print(atoi('1502'))