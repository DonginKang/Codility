#-*- coding:utf-8 -*-

'''
 A = [3, 8, 9, 7, 6]
 K = 3
 return [9, 7, 6, 3, 8]
'''

def solution(A, K):
    B = A[:]  # A ����Ʈ ����
    
    for i in range(0,len(A)):
        B[(i+K)%len(A)] = A[i] # �ٽ� �˰���  
    
    return B
    
    