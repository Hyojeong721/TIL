def itoa(number):
    result = ''
    while number > 0:
        quotient, remainder = divmod(number, 10)
        result = chr(remainder + 48) + result
        number = quotient
    return result


a = 378237800032893
print(itoa(a))

b = ['3', 'a', 'z']
print(''.join(b))

# def my_str(number):
#     digit = len(number)
#     result = 0
#     for idx, value in enumerate(number):
#         result += (ord(i) - 48) * (10 ** (digit - idx - 1))
#
# my_str()