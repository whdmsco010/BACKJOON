A = []
for i in range(5):
    row = list(input())
    A.append(row)
for i in range(len(max(A, key=len))): # 문자열의 길이 중 가장 큰 것을 반환한다.
    for j in range(5): # x축과 y축을 재배열 한다.
        try:
            print(A[j][i], end="")
        except IndexError: # Index 에러가 발생하면 건너뜀
            continue