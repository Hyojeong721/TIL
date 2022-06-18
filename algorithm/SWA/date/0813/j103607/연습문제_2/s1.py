
# 양의 정수를 문자열로 변환하는 함수 123 -> '123'
# ord() chr() 함수 사용
def itoa(number):

    my_list = []
    while number > 0:
        rest = number % 10 # rest = 3 2 1
        string = chr(ord('0')+rest) # 51 => '3' (48 => '0')
        my_list.insert(0, string)
        number = number // 10

    result = ''.join(my_list)
    return result

print(itoa(123))
