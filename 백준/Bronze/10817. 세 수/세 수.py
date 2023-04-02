import sys
input = sys.stdin.readline
A = list(map(int, input().split()))
B = sorted(A)
print(B[1])