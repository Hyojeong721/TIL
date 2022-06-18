import sys
sys.stdin = open('input.txt')
T = 10
arr = list(map(int,input()))
result = [arr[i:i+7] for i in range(0, len(arr), 7)]

ans_list=[]

for i in range(10):
    ans = 0

    for j in range(6, -1, -1):
        ans += 2**j*result[i][j]
    ans_list.append(ans)

print(*ans_list)