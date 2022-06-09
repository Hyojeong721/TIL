# def itoa(i):
#     chars = []
#     while i > 0:
#         chars.append(i % 10)
#         i = i // 10
#     chars = chars[::-1]
#     result = ''
#
#     for char in chars:
#         value = chr(char+48)
#         result += value
#
#     return result

def itoa(my_int):
    my_str = []

    while my_int != 0:
        r = my_int % 10
        char = chr(r + ord('0'))
        my_str.append(char)
        my_int //= 10
    my_str.reverse()

    result = ''.join(mytr)
    return result

print(itoa(123))



