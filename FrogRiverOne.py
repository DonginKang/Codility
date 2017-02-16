#-*- coding:utf-8 -*-

'''
Check whether array A is a permutation.

Example 
X = 5
A = [1,3,1,4,2,3,5,4]  # elements = 1~X
return 6

'''



def solution(X,A):
	B = [0] * X
	TotalSum = 0             # 전체 합계
	PartialSum = 0	         # 부분 합계
	
	for i in xrange(1,X+1):
		TotalSum += i     # 전체 합계
	
	for j in xrange(0,len(A)):
		if B[A[j]-1] == 0:                   # B배열이 비어 있으면
			B[A[j]-1] = A[j]             # B에 A값을 넣고
			PartialSum += A[j]	     # 부분합계를 누적시킨다.
			if PartialSum == TotalSum:   # 부분합계와 전체합계가 같아질때 
				return j  	     # A의 위치를 return 시킨다.
			
	return -1    # 값이 없으면 -1을 리턴한다.
