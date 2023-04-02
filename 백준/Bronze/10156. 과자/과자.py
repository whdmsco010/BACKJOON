import sys
input = sys.stdin.readline
K, N, M = map(int, input().split())
a = K*N-M
if a<0:
    print(0)
else:
    print(a)