N, M = map(int, input().split()) # 가로(행), 세로(열)
A, B = [], []
for _ in range(N): # 반복에만 중점을 둘 때 _를 사용한다
    row = list(map(int, input().split()))
    A.append(row)

for _ in range(N):
    row = list(map(int, input().split()))
    B.append(row)

for row in range(N):
    for col in range(M):
        print(A[row][col] + B[row][col], end=" ")
    print()