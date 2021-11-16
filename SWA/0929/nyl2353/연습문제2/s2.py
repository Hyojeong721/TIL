'''
str.format(value[, format_spec])

    - format_spec에 따라, value를 <<포맷된>> 표현으로 변환

    - format_spec     ::= [[fill]align][sign][#][0][width][grouping_option][.precision][type]
    - fill            ::= <any_character>
    - align           ::= | "<"(왼) | ">"(오) | "^"(중) | "="(숫자일 때, 부호와 숫자 사이 0으로 채움)
    - sign            ::= | "+" | "-" | " "(원래 부호대로)
    - width           ::= digit+ (최소 총 필드 너비)
    - grouping_option ::= | "_" | "," (구분기호 - 2/10/16진수 4자리단위, 숫자 1000단위)
    - precision       ::= digit+ (부동소수점 앞,뒤로 표시 숫자 개수)
    - type            ::= 정수   | "b" | "c" | "d" | "o" | "x" | "X" | "n" |
                          문자열 | "s" |
                          float | "e" | "E" | "f" | "F" | "g" | "G" | "%" |

'''
import sys
sys.stdin = open('input.txt')

hexa = list(input())
for i in range(len(hexa)):
    # 16진수 문자를 2진수 문자열로 변환
    binary = format(int(hexa[i], 16), 'b')

    # 4글자로 길이 맞춤
    hexa[i] = '0' * (4 - len(binary)) + binary

bi = ''.join(hexa)
ans = []

# 정확히 7bit로 나누어 떨어지지 않음 -> +1
for i in range(len(bi)//7+1):
    deci = int(bi[7*i:7*i+7], 2)
    ans.append(str(deci))

print(', '.join(ans))