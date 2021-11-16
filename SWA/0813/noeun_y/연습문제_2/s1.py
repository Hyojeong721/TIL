def itoa1(integer):
    temp = ''
    while integer > 0:
        temp = chr((integer % 10) + 48)+temp
        integer = integer // 10
    return temp

def atoi(string):
    temp = 0
    count = len(string)-1
    for i in string:
        temp += (ord(i) - 48) * (10**count)
        count -= 1
    return temp
print((itoa1(123)))
print(atoi('123'))