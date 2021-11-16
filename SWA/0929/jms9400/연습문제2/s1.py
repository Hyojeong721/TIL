def change_10(number):
    answer = []
    number2 = ''
    for k in number:
        temp = bin(int(k, 16))
        if len(temp[2:]) < 4:
            temp = '0' * (4-len(temp[2:])) + temp[2:]
        else:
            temp = temp[2:]
        number2 += temp
    n = len(number2)
    print(number2)

    for i in range(0, n, 7):
        num = number2[i: i+7]
        temp = int(num, 2)
        answer.append(temp)
    return answer

print(change_10('0F97A3'))
print(change_10('01D06079861D79F99F'))