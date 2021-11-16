'''
class int(x, base=10)

    - 숫자나 문자열 x로부터 만들어진 정수 객체를 반환.
    - 인자가 주어지지 않으면 0을 반환
    - base (진수)를 2, 8, 10, 16로 설정 가능

'''
import sys
sys.stdin = open('input.txt')

bits = input()
ans = []
for i in range(len(bits)//7):
    # 슬라이싱 된 2진수 문자열을 10진수 정수로 변환
    num = int(bits[7*i:7*i+7], 2)
    ans.append(str(num))

print(", ".join(ans))