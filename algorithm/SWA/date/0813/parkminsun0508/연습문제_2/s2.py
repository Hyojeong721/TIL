# atoi 함수
def atoi(my_str):
    value = 0
    # 순서 i
    i = 0
    # 1234 라는 글자가 있을 때, 몇번째인지
    # 길이만큼 반복할 것
    while i < len(my_str):
        # i번째 글자를 빼올 것
        char = my_str[i]
        digit = ord(char) - ord('0')
        value = value * 10 + digit
        i += 1
    return value


print(atoi('1234'))

#글자로 들어왔던 것을 숫자로 바꿔줬다.
print(type(atoi('1234')))
# 결과값 1234로 나오도록