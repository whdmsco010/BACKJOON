N = int(input())
n = list(map(int, input().split()))
count=0
a=[]
for i in n:
    count = 0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count == 2:
        a.append(i)
print(len(a))