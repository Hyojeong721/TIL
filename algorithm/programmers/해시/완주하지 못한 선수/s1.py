participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
# 정확성 테스트 pass/ 효율성 테스트 fail
# def solution(participant, completion):
#
#     for i in completion:
#         if i in participant:
#             participant.remove(i)
#     answer = participant[0]
#
#     return answer


# 해시 이용! -> 다른사람 코드
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[part] = hash(part)
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    for key,value in dic.items():
        if value == temp:
            answer = key

    return answer


# 리스트로 푼거 대박
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[len(participant)-1]

print(solution(participant, completion))

