import sys
input = sys.stdin.readline
a = list(map(int, input().split()))
b = sorted(a)
print(b[0],b[1],b[2])