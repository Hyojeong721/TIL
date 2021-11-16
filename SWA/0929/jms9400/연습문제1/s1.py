def change_10(number):
    n = len(number)
    answer = []
    for i in range(0, n, 7):
        num = number[i: i+7]
        temp = 0
        for j in range(6, -1, -1):
            temp += int(num[j])*(2**(6-j))
        answer.append(temp)
    return answer



print(change_10('0000000111100000011000000111100110000110000111100111100111111001100111'))
print(change_10('00000010001101'))