def itoa(integer, word):
    """
    정수를 문자열 숫자로 형변환하는 함수
    integer: 정수
    word: 문자열 숫자를 저장할 배열

    """
    while integer > 0:
        digit = integer % 10
        integer //= 10
        char = chr(digit + ord('0'))
        word.append(char)

    word.reverse()
    print(word)


integer = 123
word = []
itoa(integer, word)