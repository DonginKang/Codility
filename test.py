
	
A = [3,4,4,6,1,4,4]
N = 5

def solution(N, A):
	B = [0] * N
	for i in xrange(len(A)):
		if A[i] <= N:
			B[A[i]-1] += 1
		else:
			C = sorted(B)     # modify. wrong line.
			for j in xrange(len(B)):
				B[j] = C[N-1]
	return B
	
print solution(N,A)
