n = int(input())
a = list(map(int, input().split()))
l = []
for i in range(n-1, -1, -1):
    l.insert(a[i], i+1)
print(*l)