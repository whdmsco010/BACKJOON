P = int(input())
for i in range(P):
    n, s = map(str, input().split())
    S = list(s)
    for ss in S:
        print(int(n)*ss, end = '')
    print(' ')