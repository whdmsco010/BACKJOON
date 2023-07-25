while True:
    N = int(input())
    a=[]
    if N == -1:
        break
    for i in range(1, N):
        if N%i == 0: # N의 약수 중에서 N을 제외한 약수만 더함
            a.append(i) # N의 약수를 배열 a에 넣음
    if sum(a) == N:
        print(N, " = ", " + ".join(str(i) for i in a), sep="")
    else:
        print(N, "is NOT perfect.")