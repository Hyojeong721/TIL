phone_book = ["119", "97674223", "1195524421"]


# def solution(phoneBook):
#     phoneBook = sorted(phoneBook)
#
#     for p1, p2 in zip(phoneBook, phoneBook[1:]):
#         if p2.startswith(p1):
#             return False
#     return True

def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer


def solution(phone_book):
    answer = True
    dic = {}
    # dict 만들기
    for i in phone_book:
        dic[i] = hash(i)
    # 비교하기
    for numbers in phone_book:
        temp = ''
        for num in numbers:
            temp += num
            if temp in dic and temp != numbers:
                answer = False
                break

    return answer

print(solution(phone_book))