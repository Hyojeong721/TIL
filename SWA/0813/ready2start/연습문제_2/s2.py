def itoa(num):
    """정수를 인자로 받아 문자열로 변환한다.

    ex1. 123 => '123'
    ex2. -1234 => '-1234'
    """
    new_str = []
    # is_negative: 인자로 들어온 정수가 음수면 True, 양수면 False
    is_negative = False

    # 정수가 음수인 경우 처리
    if num < 0:
        is_negative = True
        num = -num

    while num:
        num, rest = divmod(num, 10)
        char = chr(rest + ord('0'))
        new_str.append(char)

    if is_negative:
        new_str.append('-')

    return ''.join(new_str[::-1])


def atoi(word):
    """문자열을 인자로 받아 정수로 변환한다.

    ex1. '123' => 123
    ex2. '-1234' => -1234
    """
    result = 0
    # is_negative: 변환한 정수가 음수면 True, 양수면 False
    is_negative = False

    # 문자열이 '-'로 시작하는 경우 처리
    if word[0] == '-':
        is_negative = True
        word = word[1:]

    for char in word:
        result *= 10
        num = ord(char) - ord('0')
        result += num

    if is_negative:
        result = -result

    return result


print(itoa(2400))             # 2400
print(itoa(4534367))          # 4534367
print(itoa(-123))             # -123
print(type(itoa(2400)))       # <class 'str'>
print(type(itoa(4534367)))    # <class 'str'>
print(type(itoa(-123)))       # <class 'str'>

print(atoi('2486'))           # 2486
print(atoi('9348500'))        # 9348500
print(atoi('-1234'))          # -1234
print(type(atoi('2486')))     # <class 'int'>
print(type(atoi('9348500')))  # <class 'int'>
print(type(atoi('-1234')))    # <class 'int'>
