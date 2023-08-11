import sys
input = sys.stdin.readline
N = int(input())
a=[]
for i in str(N):
    a.append(i) # 한 문자열씩 배열 a에 넣는다
b = list(reversed(sorted(a))) # 배열 a를 정렬한 후 뒤집는다(내림차순)
for i in b: # 배열 a 안의 원소를 하나씩 출력한다
    print(i, end="")