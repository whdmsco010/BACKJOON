A = []
for _ in range(9): # 아래의 것을 9번 반복한다
    row = list(map(int, input().split())) # 9개의 숫자를 띄어쓰기 해서 적는다
    A.append(row)
row = 0
col = 0
for i in range(9):
    for j in range(9):
        if A[i][j] >= max(map(max, A)): # 2차원 배열 안의 원소들이 최댓값과 같으면
            row = i+1
            col = j+1
print(max(map(max, A))) # A에 속한 최대값을 찾는다
print(row, col)