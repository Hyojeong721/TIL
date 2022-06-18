# itoa() 구현

def itoa(num):
    result = ''
    if num > 0:
        while num > 0:
            char = num % 10
            converted = chr(48 + char)
            result = converted + result
            num //= 10

        return result

    elif num == 0:
        return chr(48)

    else:
        num *= -1
        while num > 0:
            char = num % 10
            converted = chr(48 + char)
            result = converted + result
            num //= 10

        return '-' + result


print(itoa(1234))
print(type(itoa(1234)))

print(itoa(0))
print(type(itoa(0)))

print(itoa(-1234))
print(type(itoa(-1234)))

