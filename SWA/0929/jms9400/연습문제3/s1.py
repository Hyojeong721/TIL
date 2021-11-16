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

    password = {
        '001101': '0',
        '010011': '1',
        '111011': '2',
        '110001': '3',
        '100011': '4',
        '110111': '5',
        '001011': '6',
        '111101': '7',
        '011001': '8',
        '101111': '9',
    }
    i = 0
    while i < n:
        num = number2[i: i+6]
        if num in password:
            answer.append(password[num])
            i += 5
        i += 1
    return answer

print(change_10('0DEC'))
print(change_10('0269FAC9A0'))