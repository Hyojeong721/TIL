def itoa(my_int):
    my_str = []

    while my_int != 0:
        r = my_int % 10
        char = chr(r + ord('0'))
        my_str.append(char)
        my_int //= 10

    my_str.reverse()

    result = ''.join(my_str)
    return result

print(type(itoa(123)), itoa(123))



def atoi(my_str):
    value = 0
    i = 0

    while i < len(my_str):
        char = my_str[i]
        digit = ord(char) - ord('0')
        value = value * 10 + digit
        i += 1

    return value

print(type(atoi('1234')), atoi('1234'))