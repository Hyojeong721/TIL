# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    answer = 0
    num = str(bin(N)[2:])
    idx = 0
    if num.count('1') == 1:
        return 0
    while idx < len(num):
        if num[idx] == '1':
            cnt = 0
            for i in range(idx+1,len(num)):
                if num[i] == '0':
                    cnt += 1
                else:
                    answer = max(answer, cnt)
                    break

        idx += 1

    return answer


print(solution(51712))
print(solution(328))

#110010100000000
