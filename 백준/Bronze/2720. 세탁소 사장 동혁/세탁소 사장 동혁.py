T =  int(input())
Q = 25
D = 10
N = 5
P = 1
for i in range(T):
    S = int(input())
    q = S//Q
    d = (S - q*Q)//D
    n = (S - q*Q - d*D)//N
    p = (S - q*Q - d*D - n*N)//P
    print(q, d, n, p)