N = int(input())
for _ in range(N):
    n = int(input())
    l = []
    for _ in range(n):
        a, b = input().split()
        l.append((int(a), int(b)))
    
    l.sort()

    cnt = 1
    f = l[0][1]

    for i in range(1, n):
        if l[i][1] < f:
            cnt += 1
            f = l[i][1]

    print(cnt)