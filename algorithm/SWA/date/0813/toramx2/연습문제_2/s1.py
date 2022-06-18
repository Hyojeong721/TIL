def itoa(num):
    my_str = []
    tmp = []
    char = ''

    while num > 0:
        tmp.append(num % 10)
        num = num // 10
    my_str = list(reversed(tmp))

    for i in my_str:
        char += (chr(i+48))

    return char

def atoi(char):
    num = 0

    for i in range(len(char)):
        num += (ord(char[i])-48) * (10 ** (len(char)-i-1))

    return num

num = int(input())
print(itoa(num))

char = input()
print(atoi(char))
