import sys
sys.stdin = open('input.txt')

# baby-gin 확인
def check(p):
    global ans
    if p[0] == p[1] and p[0] == p[2]:
        arr = p[3:]
        min_num = min(arr)
        if min_num+1 in arr and min_num+2 in arr:
            ans = 1
    else:
        ans = 0
    return ans


# 순열 만들기
def per(n, k):
    global result
    if n == k:
        result += check(p)

    else:
        for i in range(n):
            if u[i]==0:
                u[i]=1
                p[k] = arr[i]
                per(n, k+1)
                u[i]=0
    return

T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input()))
    # 순열을 저장하는 배열
    p=[0]*6
    n = len(arr)
    u=[0]*6
    result = 0
    ans = 0
    per(6, 0)

    print("#{} ".format(tc), end='')
    if result > 0:
        print('baby-gin', p)
    else:
        print('no, baby-gin')
