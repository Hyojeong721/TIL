def solution(participant, completion):
    com = dict()
    for k in range(len(completion)):
        if completion[k] not in com:
            com[completion[k]] = 1
        else:
            com[completion[k]] += 1

    for p in participant:
        if p not in com or com[p] < 1:
            return p
        else:
            com[p] -= 1

