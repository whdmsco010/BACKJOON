a = "666"
n = int(input())
i=0
count=0
while(True):
    i+=1 
    if a in str(i): # 만약 증가하는 i에 666이 들어간다면
        count+=1 # 카운터를 증가시켜서 666이 포함된 숫자의 순서를 센다
        if count==n: 
            print(i)
            break