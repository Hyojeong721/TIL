# 시간 초과

from itertools import combinations

TC = int(input())

for tc in range(TC):
    n = int(input())
    if n == 0:
        continue
    else:
        cus, cat = input().split()
        categories = [cat]
        custumes = [[cus]]
        # 카테고리별(idx)로 의상 저장하기
        for num in range(n-1):
            cus, cat = input().split()

            if cat in categories:
                for idx, cate in enumerate(categories):
                    if cat == cate:
                        custumes[idx].append(cus)
            else:
                categories.append(cat)
                custumes.append([cus])
        result = 0
        for i in range(1, len(categories)+1):
            combi = list(combinations(categories, i)) #[(,),(,)]
            for com in combi: #('','')
                num = 1
                for catego in com: # ''
                    idx = categories.index(catego)
                    num *= len(custumes[idx])
                result += num

        print(result)