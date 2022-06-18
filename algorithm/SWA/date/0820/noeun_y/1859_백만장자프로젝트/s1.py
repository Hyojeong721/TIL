import sys
sys.stdin= open("input.txt")
for tc in range(1,int(input())+1):
    N = int(input())
    m_list=list(map(int,input().split()))


    maxday=m_list[-1]
    jango=0
    for day in range(len(m_list)-1,-1,-1):
        if m_list[day]<maxday:
            jango+=maxday-m_list[day]
        else:
            maxday=m_list[day]

    print("#{} {}".format(tc,jango))





# 처음 쓴 코드는 앞에서부터 자기 자신부터 맨끝까지 중에 최댓값인지 비교하면서 매수 매도를 선택하는 방식이었다.
# 계속 맥스값을 구해야하는 문제가 있고
# 맥스값까지 다른 변수에 저장하다가 맥스를 만나면 더해줘야 하는 번거로움이 있다.
# 이러한 단점을 뒤에서부터 순회하면 해결할 수 있다.
# 뒤에서부터 돌게되면 맨 뒷값을 맥스 값으로 저장하고
# 그 맥스값보다 큰값이 나타나기 전까지는 계속 "맥스값-그날의 가격"을 더하다가
# 더 큰값이 나타나면 맥스값을 갱신해주기만 하면 된다.
#
# for tc in range(1,int(input())+1):
#     N = int(input())
#     m_list=list(map(int,input().split()))
#
#     mesu=0
#     jango =0
#     result=0
#     for day in range(len(m_list)):
#
#         if m_list[day]!=max(m_list[day:]):
#             mesu+=1
#             jango+=m_list[day]
#
#         else:
#
#             result +=(m_list[day]*mesu)-jango
#             if result==0:
#                 result=0
#                 break
#             jango=0
#             mesu=0
#
#     print("#{} {}".format(tc,result))
