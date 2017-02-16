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
	TotalSum = 0             # ��ü �հ�
	PartialSum = 0			 # �κ� �հ�
	
	for i in xrange(1,X+1):
		TotalSum += i        # ��ü �հ�
	
	for j in xrange(0,len(A)):
		if B[A[j]-1] == 0:             # B�迭�� ��� ������
			B[A[j]-1] = A[j]		   # B�� A���� �ְ�
			PartialSum += A[j]		   # �κ��հ踦 ������Ų��.
			if PartialSum == TotalSum: # �κ��հ�� ��ü�հ谡 �������� 
				return j  			   # A�� ��ġ�� return ��Ų��.
			
	return -1 	 			  # ���� ������ -1�� �����Ѵ�.