import sys
input = sys.stdin.readline
N = int(input())
i=2
while True:
    if N%i==0: 
        N = N/i
        print(i)
    else:
        i+=1
    if N==1:
        break 