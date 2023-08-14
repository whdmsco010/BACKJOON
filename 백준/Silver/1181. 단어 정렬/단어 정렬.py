import sys
input = sys.stdin.readline
N = int(input())
a=[]
for i in range(0,N):
    a.append(input()[:-1]) # 슬라이싱 써야함 sys 라이브러리를 가져오기 때문
a = sorted(sorted(set(a)), key=len) # 사전 순, 길이 순으로 정렬
for i in a: # 배열 a 안의 원소를 하나씩 출력한다
    print(i)