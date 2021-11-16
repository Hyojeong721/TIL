# atoi() 구현

def atoi(text):
    result = 0

    if text[0] == '-':
        text = text[1:]
        for idx, char in enumerate(text):
            num = ord(char) - 48
            result += num * 10 ** (len(text) - 1 - idx)
        return result * (-1)
    else:
        for idx, char in enumerate(text):
            num = ord(char) - 48
            result += num * 10 ** (len(text) - 1 - idx)
        return result


print(atoi('1234'))
print(type(atoi('1234')))

print(atoi('0'))
print(type(atoi('0')))

print(atoi('-1234'))
print(type(atoi('-1234')))