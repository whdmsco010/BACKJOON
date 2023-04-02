import sys
input = sys.stdin.readline
A, B = map(str, input().split())
a = int(A[::-1])
b = int(B[::-1])
if a>b:
    print(a)
elif a<b:
    print(b)