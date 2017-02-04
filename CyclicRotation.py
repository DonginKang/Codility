#-*- coding:utf-8 -*-

'''
 problem example 
 
 A = [3, 8, 9, 7, 6]
 K = 3  
 return [9, 7, 6, 3, 8]

'''

def solution(A, K):
    B = A[:]  # A 리스트 복사
    
    for i in range(0,len(A)):
        B[(i+K)%len(A)] = A[i] # 핵심 알고리즘  
    
    return B
    
    
