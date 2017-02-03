# Binary Gap Problem

1. input int(1041)
2. 1041 =  10000010001
3. 1000001 = 0 x 5 , 10001 = 0 x 3
4. return 5

#-*- coding:utf-8 -*-

# int -> bin 변환을 위한 함수
def int2bin(i):
    if i == 0: return "0"
    s = ''
    while i:
        if i & 1 == 1:
            s = "1" + s
        else:
            s = "0" + s
        i /= 2
    return s
    
    
def solution(N):
    bin = int2bin(N) # bin 은 String 형태 
    GapLength = 0  #  1과 1 사이의 0의 길이 값을 저장하는 변수
    max = 0 # 여러 GapLength 들 중 가장 큰 값을 저장하는 변수
   
    for pos in range(0,len(bin)-1):
        if bin[pos] == '1' and bin[pos+1] == '0':
            GapLength += 1
        elif bin[pos] == '0' and bin[pos+1] == '0':
            GapLength += 1
        elif bin[pos] == '0' and bin[pos+1] == '1':
            if GapLength > max:
                max = GapLength
            GapLength = 0
    return max
