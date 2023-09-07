import sys
input = sys.stdin.readline
s = set()
t = []
cnt = 0
N, M = map(int, input().split())
for i in range(N):
    s.add(input()[:-1]) 
    # set은 add로 데이터를 추가함
    # sys 함수를 사용하면 \n이 끝에 붙게 되어 그것을 방지하기 위함
for _ in range(M):
    m = input()[:-1]
    if m in s:
        cnt += 1
print(cnt)