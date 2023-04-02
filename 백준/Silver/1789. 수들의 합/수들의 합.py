m = int(input())
sum=0
i=1
while True:
    sum = sum + i
    i += 1
    if sum>m:
        print(i-2)
        break