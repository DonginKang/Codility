#-*- coding:utf-8 -*-


'''
1. 우선 리스트를 딕셔너리 형태로 만든다.
2. 딕셔너리를 tuple로 변환한다.
3. 변환된 tuple 에서 홀수 값을 가지는 것을 반환한다.
'''

def solution(A):                    # A is List. Ex) A[0] = 9  A[1] = 3  A[2] = 9 ..
    dict = {}
    
    for pos in range(0,len(A)):
        if dic.get(A[pos]) == None: # 처음에 비어있는지 없는지 확인, 꼭 get 쓰기
            dic[A[pos]] = 1         # key - value 값 만들어 주는것
        else: dic[A[pos]] += 1      # key값이 이미 존재하면 거기다 +1 해주기
        
    tup = dic.items() # 딕셔너리를 튜플로 변환. 이유? for 함수로 돌려서 체크 할려고

    for pos in range(0,len(a)):     # 홀수 value 를 가지는 key 값 찾기
        remainder = a[pos][1] % 2
        if remainder == 1:
            return a[pos][0]        # 홀수인 value 의 key값 반환 
