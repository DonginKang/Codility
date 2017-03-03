

'''
"Manhattan skyline" using the minimum number of rectangles.
'''

H = [8,8,5,7,9,8,7,4,8]

def solution(H):
	count = 0
	for i in range(0,len(H)-1):
		if H[i] != H[i+1]:
			count += 1
			print i
	return count
		
print solution(H)