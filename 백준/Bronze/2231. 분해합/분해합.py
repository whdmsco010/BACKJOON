N = int(input())
x = 0
for i in range(1, N+1):
    a = list(map(int, str(i)))
    if i + sum(a) == N:
        x = i
        break
print(x)