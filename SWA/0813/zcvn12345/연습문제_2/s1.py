def itoa(integer):
    temp = ''
    while integer > 0:
        temp = chr((integer % 10) + 48)+temp
        integer = integer // 10
    return temp

def atoi(string):
    temp = 0
    count = len(string)
    for i in string:
        count -= 1
        temp += (ord(i) - 48) * (10**count)
    return temp

print(itoa(12345))
print(atoi('1234567'))

