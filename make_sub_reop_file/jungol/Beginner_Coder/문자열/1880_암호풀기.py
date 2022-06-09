keys = input()
password = input()

for i in password:
    if i == ' ':
        print(i, end='')
    else:
        num = ord(i)
        if 64 < num < 91:
            num -= 65
            temp = keys[num].upper()
            print(temp, end='')
        else:
            96 < num < 123
            num -= 97
            temp = keys[num]
            print(temp, end='')


