N, M = map(int, input().split())
n = [x for x in range(1,N+1)]
for a in range(M):
    i, j = map(int, input().split())
    n[i-1], n[j-1] = n[j-1], n[i-1]
for Nn in n:
    print(Nn, end=" ")
