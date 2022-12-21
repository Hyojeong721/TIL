import sys
input = sys.stdin.readline


T = int(input())
for t in range(1, T + 1):
    n = input()
    grade_cnt = [0] * 101
    mymax = 0
    grade = 0
    arr = list(map(int, input().split()))
    for i in range(len(arr)):
        grade_cnt[arr[i]] += 1
    for x in range(1, len(grade_cnt)):
        if mymax <= grade_cnt[x]:
            mymax = grade_cnt[x]
            grade = x

    print('#{} {}'.format(t, grade))
