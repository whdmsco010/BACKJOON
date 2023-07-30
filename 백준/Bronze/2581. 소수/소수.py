M = int(input())
N = int(input())
sum = 0
a= []
for i in range(M, N+1):
    count=0
    for j in range(1, i+1):
        if i%j == 0:
            count+=1
    if count == 2: # 소수만 배열에 넣어라
        sum += i
        a.append(i)
if a: # 배열이 비어있지 않으면
    print(sum) # 소수들의 합
    print(a[0]) # 소수 중 가장 작은 수
else:
    print(-1)