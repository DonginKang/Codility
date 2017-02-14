#-*- coding:utf-8 -*-

'''

Find the minimal positive integer not occurring in a given sequence.


The number of cases

1) A = [-1,-2,-4,0]
2) A = [3,2,4,5,0]
3) A = [1,1,1,1,1]
4) A = [1,2,3,4,5]
5) A = [1,1,2,3,4]

'''

A = [1,1,2,3,4]

def solution(A):
    B = []
    for i in xrange(len(A)):
        if A[i] > 0:           # A 안에 양수만 골라내서 리스트 B에 담는다.
            B.append(A[i])        
    if B == []:                # A 안에 0 or 음수만 들어있을 경우 1을 리턴한다.  1)번 케이스
        return 1
    else:
        B.sort()               # B를 정렬한다.
        if B[0] != 1:          # B의 첫번째 숫자가 1이 아닐경우 바로 1을 리턴한다.    2)번 케이스
            return 1
        if B[0] == B[len(B)-1]:     # 리스트 안의 숫자가 모두 똑같을 경우 2를 리턴한다.     3)번 케이스         
            return 2        

        for j in xrange(len(B)-1):   # B리스트의 앞 뒤를 비교한다.
            if B[j] == B[j+1] or B[j]+1 == B[j+1]:  # 앞 뒤가 같거나 1차이가 나면 그냥 무시한다.
                continue
            else:
                return B[j]+1  # 그렇지 않을경우 앞의 값에 +1 한 값을 리턴한다.
                
    return B[len(B)-1]+1   # 4)번과 5)번 케이스에서 동작한다.
    
print solution(A)
                