import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    # 첫번째 요소 뽑아서 뒤로 집어넣기 반복
    for i in range(M):
        nums.append(nums.pop(0))
    print(f'#{tc} {nums[0]}')