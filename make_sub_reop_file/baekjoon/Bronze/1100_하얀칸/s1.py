import sys
sys.stdin = open('input.txt')

arr = [input() for _ in range(8)]
cnt = 0

for row in range(1, 9):
    for col in range(1, 9):
        # 행이 홀수일 때
        if row % 2 :
            # 열은 홀수여야 흰색 칸이다.
            if col % 2:
                if arr[row-1][col-1] == 'F':
                    cnt += 1
        # 행이 짝수일 때,
        else:
            # 열이 짝수여야 흰색 칸이다.
            if col % 2 == 0:
                if arr[row-1][col-1] =='F':
                    cnt += 1

print(cnt)