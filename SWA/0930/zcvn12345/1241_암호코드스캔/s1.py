import sys
sys.stdin = open('input.txt')

decode = {'211':0, '221':1, '122':2,'411':3, '132':4,'231':5, '114':6, '312':7, '213':8, '112':9}
hex_to_bin = {'0':'0000', '1':'0001', '2':'0010', '3':'0011', '4':'0100', '5':'0101', '6':'0110', '7':'0111', '8':'1000', '9':'1001', 'A':'1010', 'B':'1011', 'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'}

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    mat = [input() for _ in range(N)]
    mat = sorted(list(set(mat)))[1:]
    # 중복제거 해도 한줄에 코드가 두개이고 다음줄에 둘중 하나만 있는 경우가 있기 때문에 중복계산 하지 않도록 리스트를 만들어줌
    code_lst = []
    result = 0
    for i in mat:
        temp = ''
        for j in i:
            temp += hex_to_bin[j]
        decimal_list = []
        n1 = n2 = n3 = 0
        for n in range(len(temp)-1, -1, -1):
            if n2 == 0 and temp[n] == '1':
                n3 += 1
            elif n3 and n1 == 0 and temp[n] == '0':
                n2 += 1
            elif temp[n] == '1':
                n1 += 1
            elif n1 and temp[n] == '0':
                x = min(n1, n2, n3)
                decimal_list.append(decode[str(n1//x) + str(n2//x) + str(n3//x)])
                # 한줄에 코드가 두개 존재하는 경우도 있기 때문에 변수 초기화
                n1 = n2 = n3 = 0
                if len(decimal_list) == 8:
                    if ((decimal_list[1] + decimal_list[3] + decimal_list[5] + decimal_list[7]) * 3 + decimal_list[0] + decimal_list[2] + decimal_list[4] + decimal_list[6]) % 10 == 0:
                        if decimal_list not in code_lst:
                            result += sum(decimal_list)
                            code_lst.append(decimal_list)
                    # 한줄에 코드가 두개 존재하는 경우도 있기 때문에 리스트 초기화
                    decimal_list = []
    print(f'#{tc} {result}')





