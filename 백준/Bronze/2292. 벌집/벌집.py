#an = 6*n + an-1
N = int(input())
a = 1
n = 0
while(1):
    a = 6*n + a
    n += 1 # n을 1씩 증가 시킴
    if N == 1:
        print(n)
        break
    if N <= a:
        print(n)
        break