a = list(map(str, input()))
b = []
UCPC = ["U", "C", "P", "C"]
idx = 0
for i in range(len(a)):
        if a[i].isupper()==True:
            b.append(a[i])
for i in b:
    if i == UCPC[idx]:
            idx+=1
            if idx == 4:
                break
if idx == 4:
            print("I love UCPC")
else:
            print("I hate UCPC")