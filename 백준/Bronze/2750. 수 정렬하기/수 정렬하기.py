N = int(input())
a=[]
for _ in range(N):
    n = int(input())
    a.append(n)
b = sorted(a)
for i in b:
    print(i)