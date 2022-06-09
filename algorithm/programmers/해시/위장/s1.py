from itertools import combinations

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]

def solution(clothes):
    dic = {}
    for i in clothes:
        if i[1] in dic:
            if type(dic[i[1]]) is not list:
                temp = dic[i[1]]
                dic[i[1]] = [temp, i[0]]
            else:
                dic[i[1]].append(i[0])
        else:
          dic[i[1]] = i[0]

    # 리스트를 가지는 key dic
    list_key_dic = {}
    for key, val in dic.items():
        if type(val) is list:
            list_key_dic[key] = len(val)

    # 만약 type(value)가 리스트이면 리스트 원소갯수만큼 곱하기
    # dic = {'headgear': ['green_turban', 'yellowhat'], 'eyewear': 'bluesunglasses',}
    # key_list_dic ={'headgear': 2}

    # dic {'face': ['crowmask', 'bluesunglasses', 'smoky_makeup']}
    # key_list_dic = {'face': 3}
    cnt = 1
    if len(dic) == 1:
        cnt = list(list_key_dic.values())[0]

    else:
        for n in range(1, len(dic)+1):
            com_list = list(combinations(list(dic.keys()), n))
            com ={}
            for lis in com_list:
                com[lis] = n
            for keys, val in com.items():
                idx = 0
                for key in keys:
                    idx += 1
                    if key in list_key_dic:
                        cnt += (com[keys]-1) * list_key_dic[key]
                    else:
                        cnt += len(keys)

        cnt = cnt-1
    return cnt
print(solution(clothes))

