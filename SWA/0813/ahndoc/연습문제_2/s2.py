def atoi(my_str):
    value = 0
    i = 0

    while i < len(my_str):
        char = my_str[i]
        digit = ord(char) - 48
        value = value * 10 + digit
        i += 1

    return value



print(atoi('123'))
