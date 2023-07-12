# 2 3 5 9 17 33
N = int(input())
n = 2
for i in range(N):
    n = n+(n-1)
print((n**2))