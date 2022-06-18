# def itoa_x(number):
#     if 65 <= number <=125:
#         for i in range(65, 125):
#             a = (chr(number))
#             # a ~ z
#         print(a)
#             break
#     else:
#         print("65~125 사이 수를 입력하시오")

def itoa(my_int):
    my_str = []

    while my_int != 0:
        r = my_int % 10

        co = chr(r +ord('0'))

        my_str.append(co)
        my_int //= 10
    my_str.reverse()
    result = ''.join(my_str)
    return result

print(itoa(123))