def itoa(a):
    lst = []
    while a > 0:
        if a < 10:
            lst.append(a)
            a = 0
        else:
            n = a % 10
            lst.append(n)
            a = a // 10
    result = ''
    str_dict ={
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
    }
    for i in lst[::-1]:
        result += str_dict[i]
    print(result)

# def itoa(my_int):
#     my_str = []
#
#     while my_int != 0
#         r = my_int % 10
#         char = chr(r + ord('0'))
#         my_str.append(char)
#         my_int //= 10
#
#     my_str.reverse()
#
#     result = ''.join(my_str)
#     print(result)


def atoi(a):
    str_dict = {
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
    }
    my_int = 0
    n = 1
    a = a[::-1]
    for i in a:
        my_int += str_dict[i] * n
        n *= 10

    print(my_int)

# def atoi(a):
#     val = 0
#     i = 0
#
#     while i <len(a):
#         char = a[i]
#         digit = ord[char] - ord('0')
#         val = val * 10 + digit
#         i += 1
#     print(val)