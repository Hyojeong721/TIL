import sys
sys.stdin = open('input.txt')

arr = input()

num_2_arr = ''
def Bbit_print(i):
    output = ""
    for m in range(3,-1,-1):
        if i & (1 << m):
            output += "1"
        else:
            output += "0"
    return output

for i in range(len(arr)):
    # 16진수를 10진수로
    num_10 = int(arr[i], 16)
    # 10진수를 2진수로
    num_2 = Bbit_print(num_10)
    num_2_arr += num_2

num_7bit = [num_2_arr[j:j+7] for j in range(0, len(num_2_arr), 7)]

ans = []
for k in range(len(num_7bit)):
    ans.append(int(num_7bit[k], 2))

print(ans)