import sys
input = sys.stdin.readline
import math
A, B, V = map(int, input().split())
n = (V-A)/(A-B) # n일
if type(n) == int:
    print(math.ceil(n))
else:
    print(math.ceil(n)+1)