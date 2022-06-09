import sys
sys.stdin = open('input.txt', 'r')

sample = input()
binary = format(int(sample, 16), 'b')

# format(value, args): value값을 args진수로 바꿔준다
# 16 -> 10 -> 2
# hex 16, oct 8, bin 2
result = [binary[i:i+7] for i in range(0, len(binary), 7)]
result = list(map(lambda x: str(int('0b'+x, 2)), result))

print(', '.join(result))



