import sys

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

def atoi(my_str):
    value = 1
    result = 0
    for num in range(len(my_str) -1, -1, -1):
        char = my_str[num]
        digit = ord(char) - ord('0')
        result += digit * value
        value *= 10

    return result

print(atoi('123'))
