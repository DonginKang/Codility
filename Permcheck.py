#-*- coding:utf-8 -*-

'''
Check whether array A is a permutation.

'''


def solution(A):
	A.sort()
	if not A[0] == 1:            
		return 0
	for i in xrange(len(A)):      #  My mistake is len(A)-1 ... 
		if not A[i] == i+1:
			return 0
			
	return 1

