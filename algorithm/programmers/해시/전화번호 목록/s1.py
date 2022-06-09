phone_book = ["12","123","1235","567","88"]# 스트링
# testcase 통과
# 정확성 -3
# 효율성 다틀림
def solution(phone_book):
    answer = True

    dic = {}
    for i in phone_book:
        dic[i] = hash(i)

    while phone_book:
        temp = phone_book.pop(0)
        del dic[temp]

        for key in dic.keys():
            if temp in key:
                answer = False
                break

    return answer

print(solution(phone_book))