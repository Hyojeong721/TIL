def atoi(my_str):
    value = 0
    i = 0

    while i < len(my_str):
        char = my_str[i]
        num = ord(char) - ord('0')
        value = value * 10 + num
        i += 1

    return value

print(atoi('1234'))
