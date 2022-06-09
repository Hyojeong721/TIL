# 자기 점수중에 최댓값 고름 = M
# 모든 점수를 점수/M*100 으로 수정

# 위의 방법대로 새로운 전체 평균을 구하는 프로그램

import sys
sys.stdin = open('input.txt')
# 시험본 과목 개수
N = int(input())

# 현재 성적
score = list(map(int, input().split()))

# 1. 최댓값 고르기
score.sort()
M = score[-1]

# 2. 모든점수 수정하기
new_score = []
total = 0
for i in range(N):
    new_score.append(score[i]/M*100)
    total += new_score[i]

# 전체평균구하기
print(total/N)