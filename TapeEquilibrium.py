#-*- coding:utf-8 -*-

'''
Minimize the value |(A[0] + ... + A[P-1]) - (A[P] + ... + A[N-1])|.
A = [3,1,2,4,3] --> return 1
'''


def solution(A):
    RightSide = sum(A)
    LeftSide = 0
    MiniDiff = None
    
    for i in xrange(0,len(A)-1):           # 그냥 숫자 반복할때는 range 보다 xrange가 더 빠르다.
        LeftSide  += A[i]                  # sum(A[:i]) 이런식으로 했다가 복잡도가 너무 높아졌다.
        RightSide -= A[i] 
        Diff = abs(LeftSide - RightSide)
    
        if MiniDiff == None:
            MiniDiff = Diff
        else:
            MiniDiff = min(MiniDiff, Diff) 
            
    return MiniDiff
    