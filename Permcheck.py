#-*- coding:utf-8 -*-

'''
Check whether array A is a permutation.

'''


def solution(A):
	A.sort()
	if not A[0] == 1:         
		return 0
	for i in xrange(len(A)):      # 내가 실수한 부분 len(A)-1 로 썻음.. 
		if not A[i] == i+1:
			return 0
			
	return 1

