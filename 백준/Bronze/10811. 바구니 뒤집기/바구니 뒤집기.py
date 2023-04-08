N, M = map(int, input().split())
n = [a for a in range(1,N+1)]
for b in range(0,M):
    i, j = map(int,input().split())
    n[i-1:j] = reversed(n[i-1:j])
for mn in n:
    print(mn, end=" ")