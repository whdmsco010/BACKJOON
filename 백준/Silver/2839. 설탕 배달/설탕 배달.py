N = int(input())
count=0
while(N>=0):
    if N%5==0: 
        count+=N//5
        print(count)
        break
    N = N-3
    count+=1
else: 
    print(-1)
# 5로 나누어 떨어지는지 판단하고 아니면 3을 뺀다
# -> 5로 묶는게 안되니 3으로 묶기 위해
# 이도 저도 아니면 -1을 출력