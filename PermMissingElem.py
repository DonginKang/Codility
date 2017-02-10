

#Find the missing element in a given permutation
A = [1,2,3,4,5] 

def solution(A):
    A.sort()
    print A
    for i in range(0,len(A)):
        if not A[i] == i+1:
            print "wow"
            return i+1
    print "last"
    return len(A) + 1
        
   
print solution(A)
