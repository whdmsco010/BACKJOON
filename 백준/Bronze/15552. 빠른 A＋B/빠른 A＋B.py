import sys
T = int(sys.stdin.readline().rstrip())
for i in range(0,T):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    print(A+B)