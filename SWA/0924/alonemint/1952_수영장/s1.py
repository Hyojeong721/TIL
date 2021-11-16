import sys
sys.stdin = open('sample_input.txt')

T = int(input())

def dfs(months, month, total):
    global min_total
    if month >= 13:
        if total < min_total:
            min_total = total
        return
    elif total > min_total:
        return
    else:
        dfs(months, month+1, total+months[month]*fee[0])
        dfs(months, month+1, total+fee[1])
        dfs(months, month+3, total+fee[2])

for tc in range(1, T+1):
    #1일, 1달, 3달, 1년
    fee = list(map(int, input().split()))
    months = [0] + list(map(int, input().split()))
    min_total = fee[3]
    dfs(months, 1, 0)
    print(f'#{tc} {min_total}')