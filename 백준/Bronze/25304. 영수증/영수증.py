X = int(input())
N = int(input())
sum = 0
for i in range(0,N):
    a, b = map(int, input().split())
    c = a*b
    sum = sum + c
if (X == sum):
    print("Yes")
else:
    print("No")