import sys
input = sys.stdin.readline
sum = 0
A = int(input())
a = int(input())
N = list(map(int, str(a)))
for n in N:
    sum = sum + n
print(sum)