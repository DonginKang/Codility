#-*-coding:utf-8 -*-


def solution(A):
	dic = dict()
	
	for i in range(0,len(A)):  # len(A)-1 을 왜 했지.. 
		if dic.get(A[i]) == None:
			dic[A[i]] = 1
			
	return len(dic.keys()) 
	
