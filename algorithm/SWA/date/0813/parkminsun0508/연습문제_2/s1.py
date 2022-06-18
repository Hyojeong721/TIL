# itoa 사용하기

def itoa(my_int):
    # my_str이라는 리스트를 만들 것
    # 1, 2, 3을 하나씩 끊어서 만들고, 문자열로 만들어 줄 것
    my_str = []
    # 10 씩 나눠줄 것
    # 0 이면 그만두라고 할 것
    while my_int != 0:
        r = my_int % 10
        # 글자를 연산하기 위한 방법
        char = chr(r + ord('0'))
        my_str.append(char)
        # my_int = my_int // 10
        my_int //= 10
    my_str.reverse()

    result = ''.join(my_str)
    return result


print(itoa(123))

print(type(itoa(123)))
# 글자로 변환되었음을 확인할 수 있다.
# => '123' 출력값 나와야함

# 글자로 바꾸면 iterable 가능한 객체가 된다. 그러면 for 문 사용이 가능하다.