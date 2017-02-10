#-*- coding:utf-8 -*-

# Problem : Find the missing element in a given permutation

'''
A = [1 ~~ (N+1)]

A = [1,2,3,4,6]  return 5
A = [1,2,3,4,5]  return 6  문제 잘 읽자, 마지막에 무조건 N+1 이 들어간다.  

'''
def solution(A):
    A.sort()   # B = sorted(A) 로도 쓸 수 있다.
    print A
    for i in range(0,len(A)):
        if not A[i] == i+1:
            return i+1
    return len(A) + 1
        