import sys
sys.stdin = open('input.txt')

# 추천하면 사진틀에 입력
# 사진틀꽉찼으면 제일 작은 표를 가진 사진 아웃 후에 새로운학생 추가
# 젤 작은표가 2명이면 가장 오래된 사진 삭제

N = int(input())
T = int(input())
arr = list(map(int, input().split()))

members = {}
photo = []

def able(tool):
    return len(tool) < N

def small(tool):
    change_idx = tool[0][1]
    temp = 99999
    for k in range(len(tool)):
        if temp > tool[k][1]:
            change_idx = k
            temp = tool[k][1]

    return change_idx

def search(arr, num):
    for idx in range(len(arr)):
        if arr[idx][0] == num:
            return idx
    return -1

for k in range(T):
    idx = search(photo, arr[k])

    if idx != -1:
        photo[idx][1] += 1
    else:
        if able(photo):
            photo.append([arr[k], 1, k])
        else:
            out_idx = small(photo)
            del photo[out_idx]
            photo.append([arr[k], 1, k])


photo.sort()

for i in range(len(photo)):
    print(photo[i][0], end = ' ')
