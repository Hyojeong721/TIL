import sys
sys.stdin = open('input.txt')

bits = input()
ans = []
for i in range(len(bits)//7):
    num = int(bits[7*i:7*i+7], 2)
    ans.append(str(num))

print(", ".join(ans))

