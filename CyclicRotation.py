#-*- coding:utf-8 -*-

'''
 problem example 
 
 A = [3, 8, 9, 7, 6]
 K = 3  # move 3
 return [9, 7, 6, 3, 8]

'''

def solution(A, K):
    B = [0] * len(A)  # Making list space like A 
    
    for i in range(0,len(A)):
        B[(i+K)%len(A)] = A[i] # Key Algorithm   
    
    return B
    
    
